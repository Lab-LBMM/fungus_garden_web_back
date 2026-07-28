from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Gene(Base):
    __tablename__ = "gene"

    gene_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    gene_name = Column(String(100), nullable=True)
    locus_tag = Column(String(50), nullable=False)
    gbkey = Column(String(50), nullable=False)
    start_pos = Column(Integer, nullable=False)
    end_pos = Column(Integer, nullable=False)
    strand = Column(String(1), nullable=False)
    predicted_product = Column(Text, nullable=True)
    
    '''FOREIGN KEY RELATIONSHIPS AND RELATIONSHIPS'''
    seq_genome_id = Column(Integer, ForeignKey("genome_sequence.seq_genome_id"), nullable=False)
    genome_sequence = relationship("GenomeSequence", back_populates="genes")
    nucleotide_sequence = relationship("NucleotideSequence", back_populates="gene", uselist=False)
    proteins = relationship("Protein", back_populates="gene")
