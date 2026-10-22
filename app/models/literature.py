from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Literature(Base):
    __tablename__ = "literature"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text, nullable=True)
    author = Column(Text, nullable=True)
    year = Column(Integer, nullable=True)
    doi = Column(String(255), nullable=True, unique=True)
