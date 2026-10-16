from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class ProteinSequence(Base):
    __tablename__ = "protein_sequences"

    id             = Column(Integer, primary_key=True, autoincrement=True, index=True)
    seq_identifier = Column(String(255), unique=True, nullable=False)
    sequence       = Column(Text,    nullable=False)
    seq_length     = Column(Integer, nullable=False)
    # 1:1 com Protein (unique=True garante a cardinalidade)
    protein_id     = Column(Integer, ForeignKey("proteins.id", ondelete="CASCADE"), nullable=False, unique=True)

    # ── Relacionamentos ──────────────────────────────────────────────────────
    protein = relationship("Protein", back_populates="protein_sequence")
