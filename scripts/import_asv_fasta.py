"""Import ASV FASTA records from a .fasta.gz file into the asvs table."""

import argparse
import gzip
import re
import sys
from pathlib import Path
from typing import Iterator, TextIO

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.database import SessionLocal  # noqa: E402
from app.Models.asv import ASV  # noqa: E402


DNA_BASES = re.compile(r"^[ACGTRYSWKMBDHVN]+$", re.IGNORECASE)
MARKER = "16S"


def read_fasta(handle: TextIO) -> Iterator[tuple[str, str]]:
    """Yield (lab identifier, sequence) records from a FASTA stream."""
    identifier = None
    sequence_parts: list[str] = []

    for line_number, raw_line in enumerate(handle, start=1):
        line = raw_line.strip()
        if not line:
            continue

        if line.startswith(">"):
            if identifier is not None:
                yield identifier, _validated_sequence(identifier, sequence_parts)
            header = line[1:].strip()
            if not header:
                raise ValueError(f"Cabeçalho FASTA vazio na linha {line_number}.")
            identifier = header.split()[0]
            sequence_parts = []
            continue

        if identifier is None:
            raise ValueError(f"Sequência antes do primeiro cabeçalho FASTA (linha {line_number}).")

        sequence_parts.append("".join(line.split()).upper())

    if identifier is not None:
        yield identifier, _validated_sequence(identifier, sequence_parts)


def _validated_sequence(identifier: str, parts: list[str]) -> str:
    sequence = "".join(parts)
    if not sequence:
        raise ValueError(f"O registro {identifier} não contém sequência.")
    if not DNA_BASES.fullmatch(sequence):
        raise ValueError(f"O registro {identifier} contém caracteres que não são bases IUPAC de DNA.")
    return sequence


def load_records(fasta_path: Path) -> dict[str, str]:
    records: dict[str, str] = {}
    with gzip.open(fasta_path, mode="rt", encoding="utf-8") as fasta:
        for identifier, sequence in read_fasta(fasta):
            previous = records.get(identifier)
            if previous is not None and previous != sequence:
                raise ValueError(f"O identificador {identifier} aparece com sequências diferentes no FASTA.")
            records[identifier] = sequence

    if not records:
        raise ValueError("O arquivo FASTA não contém registros.")
    return records


def import_asvs(fasta_path: Path) -> tuple[int, int]:
    records = load_records(fasta_path)
    inserted = 0
    skipped = 0

    with SessionLocal.begin() as session:
        existing = set(session.scalars(select(ASV.unique_identifier)).all())
        new_records = [
            ASV(unique_identifier=identifier, marker=MARKER, sequence=sequence)
            for identifier, sequence in records.items()
            if identifier not in existing
        ]
        skipped = len(records) - len(new_records)
        session.add_all(new_records)
        inserted = len(new_records)

    return inserted, skipped


def main() -> None:
    parser = argparse.ArgumentParser(description="Importa ASVs de um FASTA compactado (.gz).")
    parser.add_argument("fasta_gz", type=Path, help="Caminho para o arquivo .fasta.gz")
    args = parser.parse_args()

    if not args.fasta_gz.is_file():
        parser.error(f"Arquivo não encontrado: {args.fasta_gz}")

    inserted, skipped = import_asvs(args.fasta_gz)
    print(f"Importação concluída: {inserted} inseridas, {skipped} já existentes ignoradas.")


if __name__ == "__main__":
    main()
