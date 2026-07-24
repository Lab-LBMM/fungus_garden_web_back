from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Protein(Base):
    __tablename__ = "protein"

    protein_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    protein_accession = Column(String(50), unique=True, nullable=False)
    protein_name = Column(String(255), nullable=False)
    product = Column(Text, nullable=False)
    aa_length = Column(Integer, nullable=False)
    
    '''FOREIGN KEY RELATIONSHIPS AND RELATIONSHIPS'''
    gene_id = Column(Integer, ForeignKey("gene.gene_id"), nullable=False)
    gene = relationship("Gene", back_populates="proteins")
    protein_sequence = relationship("ProteinSequence", back_populates="protein", uselist=False)