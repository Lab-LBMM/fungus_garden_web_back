from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Gene(Base):
    __tablename__ = "genes"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    organism_id = Column(Integer,ForeignKey("organism.organism_id"),nullable=False)
    name = Column(String(100), nullable=True)
    accession = Column(String(100),nullable=True )
    description = Column(Text,nullable=True)
    locus_tag = Column(String(50), nullable=False)
    gbkey = Column(String(50), nullable=False)
    start_pos = Column(Integer, nullable=False)
    end_pos = Column(Integer, nullable=False)
    strand = Column(String(1), nullable=False)
    predicted_product = Column(Text, nullable=True)

    proteins = relationship("Protein",back_populates="gene")

