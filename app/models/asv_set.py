from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from app.database import Base


class ASVSet(Base):
    __tablename__ = "asv_sets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sequencing_run_id = Column(
        Integer,
        ForeignKey("sequencing_runs.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    asv_id = Column(
        Integer,
        ForeignKey("asvs.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    asv_count = Column(Integer, nullable=True)


