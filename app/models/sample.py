from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Sample(Base):
    __tablename__ = "sample"

    sample_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False)
    location = Column(String(150), nullable=True)
    description = Column(Text, nullable=True)
