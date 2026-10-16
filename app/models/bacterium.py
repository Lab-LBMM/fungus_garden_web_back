from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Bacterium(Base):
    __tablename__ = "bacterium"

    organism_id             = Column(Integer, ForeignKey("organisms.id", ondelete="CASCADE"), primary_key=True)
    gram_stain              = Column(String(50),  nullable=True)
    motility                = Column(String(100), nullable=True)
    spores                  = Column(String(100), nullable=True)
    optimum_temperature     = Column(String(100), nullable=True)
    antibiotic_production   = Column(String(255), nullable=True)

    # ── Relacionamentos ──────────────────────────────────────────────────────
    organism = relationship("Organism", back_populates="bacterium")
