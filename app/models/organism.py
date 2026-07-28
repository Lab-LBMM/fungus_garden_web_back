from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Organism(Base):
    __tablename__ = "organism"

    organism_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False)
    organism_type = Column(String(150), nullable=False)  # ex: "ant", "fungus", "bacteria"
    observations = Column(String(250), nullable=True)

    '''RELATIONSHIPS'''
    genomes = relationship("Genome", back_populates="organism")
    ant = relationship("Ant", back_populates="organism", uselist=False)
    fungus = relationship("Fungus", back_populates="organism", uselist=False)
    bacteria = relationship("Bacteria", back_populates="organism", uselist=False)