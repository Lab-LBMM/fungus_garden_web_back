from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class ASV(Base):
    __tablename__ = "asvs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    unique_identifier = Column(String(100), nullable=False, unique=True, index=True)
    marker = Column(String(20), nullable=False)
    sequence = Column(Text, nullable=False)
