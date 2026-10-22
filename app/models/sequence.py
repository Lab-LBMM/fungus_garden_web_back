from sqlalchemy import Column, Date, Integer, Numeric, Text

from app.database import Base


class Sequence(Base):
    __tablename__ = "sequences"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sequence_length = Column(Integer, nullable=True)
    abundance = Column(Numeric(12, 8), nullable=True)
    fasta_sequence = Column(Text, nullable=True)
    fasta_date = Column(Date, nullable=True)
    base_sequence = Column(Text, nullable=True)
