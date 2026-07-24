from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class GenomeSequence(Base):
    __tablename__ = "genome_sequence"

    seq_genome_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    accession_seq = Column(String(50), nullable=False, unique=True)
    name_seq = Column(String(100), nullable=False)
    type_seq = Column(String(50), nullable=False)
    length = Column(Integer, nullable=False)
    nucleotide_seq = Column(Text, nullable=False)
    
    '''FOREIGN KEY RELATIONSHIP AND RELATIONSHIPS'''
    genome_id = Column(Integer, ForeignKey("genome.genome_id"), nullable=False)
    genome = relationship("Genome", back_populates="genome_sequences")
    genes = relationship("Gene", back_populates="genome_sequence")