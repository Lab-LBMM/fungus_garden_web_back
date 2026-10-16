from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Gene(Base):
    """
    Gene anotado em uma sequência genômica.
    Hierarquia: Gene → GenomeSequence → Genome → Organism
    """
    __tablename__ = "genes"

    id                = Column(Integer, primary_key=True, autoincrement=True, index=True)
    genome_sequence_id = Column(Integer, ForeignKey("genome_sequences.id", ondelete="CASCADE"), nullable=False, index=True)
    name              = Column(String(100), nullable=True)
    accession         = Column(String(100), nullable=True)
    description       = Column(Text,        nullable=True)
    locus_tag         = Column(String(50),  nullable=False)
    gbkey             = Column(String(50),  nullable=False)
    start_pos         = Column(Integer,     nullable=False)
    end_pos           = Column(Integer,     nullable=False)
    strand            = Column(String(1),   nullable=False)   # '+' ou '-'
    predicted_product = Column(Text,        nullable=True)

    # ── Relacionamentos ──────────────────────────────────────────────────────
    genome_sequence     = relationship("GenomeSequence", back_populates="genes")
    nucleotide_sequence = relationship("NucleotideSequence", back_populates="gene", uselist=False)
    proteins            = relationship("Protein", back_populates="gene")
