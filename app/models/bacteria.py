from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

'''ASSOCIATION TABLE (many-to-many with Ant)'''
ant_bacteria = Table(
    "ant_bacteria",
    Base.metadata,
    Column("ant_id", Integer, ForeignKey("ant.ant_id"), primary_key=True),
    Column("bacteria_id", Integer, ForeignKey("bacteria.bacteria_id"), primary_key=True),
)


class Bacteria(Base):
    __tablename__ = "bacteria"

    bacteria_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    genus = Column(String(100), nullable=False)
    species = Column(String(100), nullable=True)
    role = Column(String(100), nullable=True)  # ex: "defesa antifúngica", "simbionte"
    description = Column(Text, nullable=True)

    '''FOREIGN KEY RELATIONSHIP AND RELATIONSHIPS'''
    organism_id = Column(Integer, ForeignKey("organism.organism_id"), nullable=False, unique=True)
    organism = relationship("Organism", back_populates="bacteria")

    ants = relationship("Ant", secondary=ant_bacteria, back_populates="bacteria")