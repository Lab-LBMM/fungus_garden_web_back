from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class OrganismReference(Base):
    __tablename__ = "organism_references"
    id = Column(Integer,primary_key=True,autoincrement=True)
    organism_id = Column(Integer,ForeignKey("organism.id", ondelete="CASCADE"),nullable=False)
    citation = Column(Text,nullable=False )
    organism = relationship("Organism",back_populates="organism_references")