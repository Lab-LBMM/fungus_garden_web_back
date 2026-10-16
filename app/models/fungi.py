from sqlalchemy import Column, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import relationship

from app.database import Base


class Fungi(Base):
    __tablename__ = "fungi"

    organism_id           = Column(Integer, ForeignKey("organisms.id", ondelete="CASCADE"), primary_key=True)
    spores                = Column(String(100), nullable=True)
    symbiotic_role        = Column(String(255), nullable=True)   # 'Cultivar Primário' | 'Micopatógeno' | ...
    mycelium_type         = Column(String(100), nullable=True)
    growth_substrate      = Column(String(255), nullable=True)
    enzymatic_activity    = Column(JSON,        nullable=True)
    gongylidia_production = Column(String(255), nullable=True)

    # ── Relacionamentos ──────────────────────────────────────────────────────
    organism = relationship("Organism", back_populates="fungis")
