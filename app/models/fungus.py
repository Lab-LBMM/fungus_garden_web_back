from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

'''ASSOCIATION TABLE (many-to-many with Ant)'''
ant_fungus = Table(
    "ant_fungus",
    Base.metadata,
    Column("ant_id", Integer, ForeignKey("ant.ant_id"), primary_key=True),
    Column("fungus_id", Integer, ForeignKey("fungus.fungus_id"), primary_key=True),
)


class Fungus(Base):
    __tablename__ = "fungus"

    fungus_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    genus = Column(String(100), nullable=False)
    species = Column(String(100), nullable=True)
    role = Column(String(100), nullable=True)  # ex: "cultivar principal", "parasita"
    description = Column(Text, nullable=True)

    '''FOREIGN KEY RELATIONSHIP AND RELATIONSHIPS'''
    organism_id = Column(Integer, ForeignKey("organism.organism_id"), nullable=False, unique=True)
    organism = relationship("Organism", back_populates="fungus")

    ants = relationship("Ant", secondary=ant_fungus, back_populates="fungi")