from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
    CheckConstraint
)
from sqlalchemy.orm import relationship

from app.database import Base


class OrganismAssociation(Base):
    __tablename__ = "organism_associations"
    source_id = Column(Integer,ForeignKey("organism.id", ondelete="CASCADE"),primary_key=True)
    target_id = Column(Integer,ForeignKey("organism.id", ondelete="CASCADE"),primary_key=True)
    relationship = Column(Text,nullable=True )
    source = relationship("Organism",foreign_keys=[source_id],back_populates="associations_source")
    target = relationship("Organism",foreign_keys=[target_id],back_populates="associations_target")
    __table_args__ = ( CheckConstraint( "source_id <> target_id", name="check_different_organisms"),)