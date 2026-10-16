from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class GenomeSequence(Base):
    """
    Representa um scaffold, cromossomo ou contig dentro de um genoma montado.
    Hierarquia: GenomeSequence → Genome → Organism
    """
    __tablename__ = "genome_sequences"

    id             = Column(Integer, primary_key=True, autoincrement=True, index=True)
    accession_seq  = Column(String(50),  nullable=False, unique=True)
    name_seq       = Column(String(100), nullable=False)
    type_seq       = Column(String(50),  nullable=False)   # 'chromosome' | 'scaffold' | 'contig'
    length         = Column(Integer,     nullable=False)
    nucleotide_seq = Column(Text,        nullable=False)
    genome_id      = Column(Integer, ForeignKey("genomes.id", ondelete="CASCADE"), nullable=False, index=True)

    # ── Relacionamentos ──────────────────────────────────────────────────────
    genome = relationship("Genome", back_populates="genome_sequences")
    genes  = relationship("Gene",   back_populates="genome_sequence")
