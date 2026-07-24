from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class NucleotideSequence(Base):
    __tablename__ = "nucleotide_sequence"

    nuc_seq_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    identifier_seq = Column(String(255), nullable=True, unique=True)
    sequence = Column(Text, nullable=False)
    seq_length = Column(Integer, nullable=False)
    
    '''FOREIGN KEY RELATIONSHIP AND RELATIONSHIPS'''
    gene_id = Column(Integer, ForeignKey("gene.gene_id"), nullable=False, unique=True)
    gene = relationship("Gene", back_populates="nucleotide_sequence")