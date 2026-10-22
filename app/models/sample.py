from sqlalchemy import Column, ForeignKey, Integer, String, Text

from app.database import Base


class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True, autoincrement=True)
    organism_id = Column(Integer, ForeignKey("organisms.id", ondelete="CASCADE"), nullable=True, index=True)
    organism_count = Column(Integer, nullable=True)
    origin = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
