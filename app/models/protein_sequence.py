from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class ProteinSequence(Base):
    __tablename__ = "protein_sequence"

    prot_seq_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    seq_identifier = Column(String(255), unique=True, nullable=False)
    sequence = Column(Text, nullable=False)
    seq_length = Column(Integer, nullable=False)
    
    
    '''FOREIGN KEY RELATIONSHIP AND RELATIONSHIPS'''
    protein_id = Column(Integer, ForeignKey("protein.protein_id"), nullable=False, unique=True)
    protein = relationship("Protein", back_populates="protein_sequence")

    
    