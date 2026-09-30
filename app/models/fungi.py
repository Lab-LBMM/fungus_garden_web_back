from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Fungi(Base):
    __tablename__ = "fungi_attributes"

    id = Column(Integer,ForeignKey("organism.id"),primary_key=True)
    spores = Column(String(100),nullable=True)
    symbiotic_role = Column(String(255),nullable=True )
    mycelium_type = Column( String(100), nullable=True)
    growth_substrate = Column(String(255),nullable=True)
    enzymatic_activity = Column(JSON,nullable=True )
    gongylidia_production = Column(String(255),nullable=True)
    organism = relationship( "Organism",back_populates="fungis")