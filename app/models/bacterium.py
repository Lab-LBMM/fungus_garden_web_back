from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Bacterium(Base):
    __tablename__ = "bacterium"
    organism_id = Column(Integer,ForeignKey("organism.id"),primary_key=True)
    gram_stain = Column( String(50), nullable=True)
    motility = Column(String(100), nullable=True)
    spores = Column(String(100),nullable=True)
    optimum_temperature = Column( String(100),nullable=True)
    antibiotic_production = Column(String(255),nullable=True)
    organism = relationship( "Organism", back_populates="bacterium")