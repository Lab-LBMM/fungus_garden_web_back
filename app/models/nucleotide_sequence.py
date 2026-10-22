from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class NucleotideSequence(Base):
    __tablename__ = "nucleotide_sequences"

    id             = Column(Integer, ForeignKey("sequences.id", ondelete="CASCADE"), primary_key=True)
    nucleotide_chain = Column(Text, nullable=True)
    identifier_seq = Column(String(255), nullable=True, unique=True)
    sequence       = Column(Text,    nullable=False)
    seq_length     = Column(Integer, nullable=False)
    # 1:1 com Gene (unique=True garante a cardinalidade)
    gene_id        = Column(Integer, ForeignKey("genes.id", ondelete="CASCADE"), nullable=False, unique=True)

    # ── Relacionamentos ──────────────────────────────────────────────────────
    gene = relationship("Gene", back_populates="nucleotide_sequence")
