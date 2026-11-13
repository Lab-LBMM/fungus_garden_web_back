from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.database import Base


class OrganismReference(Base):
    __tablename__ = "organism_references"

    id          = Column(Integer, primary_key=True, autoincrement=True)
    organism_id = Column(Integer, ForeignKey("organisms.id", ondelete="CASCADE"), nullable=False, index=True)
    citation    = Column(Text, nullable=False)

    # ── Relacionamentos ──────────────────────────────────────────────────────
    organism = relationship("Organism", back_populates="organism_references")
