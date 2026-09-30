from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.database import Base

class Ant(Base):
    __tablename__ = "ant_attributes"
    
    organism_id = Column(Integer,ForeignKey("organism.id", ondelete="CASCADE"),primary_key=True)
    caste_system = Column(JSON, nullable=True)
    nest_depth = Column(String(255), nullable=True)
    colony_size = Column(String(255), nullable=True)
    agriculture_type = Column(String(100), nullable=True)
    organism = relationship("Organism",back_populates="ants")