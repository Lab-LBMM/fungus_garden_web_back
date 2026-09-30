from sqlalchemy import Column, Integer, Integer, Text, ForeignKey, Enum, UniqueConstraint
from sqlalchemy.orm import relationship

from app.database import Base


class Taxa(Base):
    __tablename__ = "taxa"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(Text,nullable=False)
    rank = Column(
        Enum(
            "reino",
            "filo",
            "classe",
            "ordem",
            "superfamilia",
            "familia",
            "subfamilia",
            "genero",
            "especie",
            name="taxonomic_rank"
        ),nullable=False)
    parent_id = Column(Integer,ForeignKey("taxa.id", ondelete="CASCADE"),nullable=True)
    ncbi_taxid = Column(Integer,nullable=True)
    parent = relationship("Taxa",remote_side=[id],back_populates="children")
    children = relationship("Taxa",back_populates="parent" )
    __table_args__ = (
        UniqueConstraint(
            "name",
            "rank",
            "parent_id",
            name="uq_taxa_name_rank_parent"
        ),
    )