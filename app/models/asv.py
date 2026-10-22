from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Text

from app.database import Base


class ASV(Base):
    __tablename__ = "asvs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    target_type = Column(String(100), nullable=True)
    species_name = Column(String(255), nullable=True)
    relative_abundance = Column(Numeric(12, 8), nullable=True)
    length_bp = Column(Integer, nullable=True)
    confidence = Column(Numeric(5, 4), nullable=True)
    description = Column(Text, nullable=True)
    read_count = Column(Integer, nullable=True)
    