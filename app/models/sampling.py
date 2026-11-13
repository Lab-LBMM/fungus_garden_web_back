from sqlalchemy import Column, ForeignKey, Integer

from app.database import Base


class Sampling(Base):
    __tablename__ = "samplings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sample_id = Column(Integer, ForeignKey("samples.id", ondelete="CASCADE"), nullable=False, index=True)
    sample_count = Column(Integer, nullable=True)
    ant_id = Column(Integer, ForeignKey("organisms.id", ondelete="CASCADE"), nullable=True, index=True)
   
