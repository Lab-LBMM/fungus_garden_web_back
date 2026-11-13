from sqlalchemy import Column, ForeignKey, Integer

from app.database import Base


class LiteratureReference(Base):
    __tablename__ = "literature_references"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sample_id = Column(Integer, ForeignKey("samples.id", ondelete="CASCADE"), nullable=False, index=True)
    literature_id = Column(Integer, ForeignKey("literature.id", ondelete="CASCADE"), nullable=False, index=True)
    literature_count = Column(Integer, nullable=True)
