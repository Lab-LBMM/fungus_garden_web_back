from sqlalchemy import Column, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import relationship

from app.database import Base


class Ant(Base):
    __tablename__ = "ant_attributes"

    organism_id      = Column(Integer, ForeignKey("organisms.id", ondelete="CASCADE"), primary_key=True)
    caste_system     = Column(JSON,        nullable=True)
    nest_depth       = Column(String(255), nullable=True)
    colony_size      = Column(String(255), nullable=True)
    agriculture_type = Column(String(100), nullable=True)

    # ── Relacionamentos ──────────────────────────────────────────────────────
    organism = relationship("Organism", back_populates="ants")
