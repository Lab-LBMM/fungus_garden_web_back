from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

class AgricultureType(Base):
    __tablename__ = "agriculture_type"

    agriculture_type_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(Text, nullable=True)

    '''RELATIONSHIPS'''
    ants = relationship("Ant", back_populates="agriculture_type")