from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.fungus import ant_fungus
from app.models.bacteria import ant_bacteria

class Ant(Base):
    __tablename__ = "ant"

    ant_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    genus = Column(String(100), nullable=False)
    species = Column(String(100), nullable=False)
    common_name = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)

    '''FOREIGN KEY RELATIONSHIPS'''
    organism_id = Column(Integer, ForeignKey("organism.organism_id"), nullable=False, unique=True)
    organism = relationship("Organism", back_populates="ant")

    agriculture_type_id = Column(Integer, ForeignKey("agriculture_type.agriculture_type_id"), nullable=False)
    agriculture_type = relationship("AgricultureType", back_populates="ants")

    fungi = relationship("Fungus", secondary=ant_fungus, back_populates="ants")
    bacteria = relationship("Bacteria", secondary=ant_bacteria, back_populates="ants")