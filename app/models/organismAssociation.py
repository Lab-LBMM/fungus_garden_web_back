from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.database import Base


class OrganismAssociation(Base):
    __tablename__ = "organism_associations"

    source_id        = Column(Integer, ForeignKey("organisms.id", ondelete="CASCADE"), primary_key=True)
    target_id        = Column(Integer, ForeignKey("organisms.id", ondelete="CASCADE"), primary_key=True)
    # Renomeado de 'relationship' (palavra reservada do SQLAlchemy ORM) para 'association_type'
    association_type = Column(Text, nullable=True)

    # ── Relacionamentos ──────────────────────────────────────────────────────
    source = relationship("Organism", foreign_keys=[source_id], back_populates="associations_source")
    target = relationship("Organism", foreign_keys=[target_id], back_populates="associations_target")

    __table_args__ = (
        CheckConstraint("source_id <> target_id", name="check_different_organisms"),
    )
