from sqlalchemy import Column, ForeignKey, Integer

from app.database import Base


class SampleConfection(Base):
    __tablename__ = "sample_confections"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sample_id = Column(Integer, ForeignKey("samples.id", ondelete="CASCADE"), nullable=True, index=True)
    organism_id = Column(Integer, ForeignKey("organisms.id", ondelete="CASCADE"), nullable=True, index=True)
    organism_count = Column(Integer, nullable=True)
