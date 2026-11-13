from sqlalchemy import Column, DateTime, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Organism(Base):
    __tablename__ = "organisms"

    id         = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name       = Column(String(255), nullable=False)
    common_name = Column(String(255), nullable=True)
    type       = Column(String(20), nullable=False)   # 'Formiga' | 'Fungo' | 'Bacteria'
    morphology = Column(Text, nullable=True)
    tags       = Column(JSON, nullable=True)
    image_url  = Column(String(500), nullable=True)
    color      = Column(String(7), nullable=True)
    taxon_id   = Column(Integer, ForeignKey("taxa.id"), nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    # ── Relacionamentos ──────────────────────────────────────────────────────
    taxon       = relationship("Taxa", backref="organisms")
    ants        = relationship("Ant",        back_populates="organism", uselist=False)
    bacterium   = relationship("Bacterium",  back_populates="organism", uselist=False)
    fungis      = relationship("Fungi",      back_populates="organism", uselist=False)
    genomes     = relationship("Genome",     back_populates="organism")   # 1:N — um organismo pode ter múltiplos genomas
    organism_detail     = relationship("OrganismDetail",    back_populates="organism", uselist=False)
    organism_references = relationship("OrganismReference", back_populates="organism")
    associations_source = relationship(
        "OrganismAssociation",
        foreign_keys="OrganismAssociation.source_id",
        back_populates="source",
    )
    associations_target = relationship(
        "OrganismAssociation",
        foreign_keys="OrganismAssociation.target_id",
        back_populates="target",
    )
