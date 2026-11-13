from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class SequencingRun(Base):
    __tablename__ = "sequencing_runs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    project_title = Column(Text, nullable=True)
    target_gene = Column(String(100), nullable=True)
    sequencing_depth = Column(Integer, nullable=True)
