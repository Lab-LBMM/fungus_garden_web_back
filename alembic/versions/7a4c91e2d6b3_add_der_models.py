"""add DER models

Revision ID: 7a4c91e2d6b3
Revises: 3c5d0cce924d
Create Date: 2026-10-22

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "7a4c91e2d6b3"
down_revision: Union[str, None] = "3c5d0cce924d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "samples",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("organism_id", sa.Integer(), nullable=True),
        sa.Column("organism_count", sa.Integer(), nullable=True),
        sa.Column("origin", sa.String(length=255), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["organism_id"], ["organisms.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_samples_organism_id", "samples", ["organism_id"], unique=False)

    op.create_table(
        "literature",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("title", sa.Text(), nullable=True),
        sa.Column("author", sa.Text(), nullable=True),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("doi", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("doi"),
    )

    op.create_table(
        "sequences",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("sequence_length", sa.Integer(), nullable=True),
        sa.Column("abundance", sa.Numeric(precision=12, scale=8), nullable=True),
        sa.Column("fasta_sequence", sa.Text(), nullable=True),
        sa.Column("fasta_date", sa.Date(), nullable=True),
        sa.Column("base_sequence", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "sequencing_runs",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("project_title", sa.Text(), nullable=True),
        sa.Column("target_gene", sa.String(length=100), nullable=True),
        sa.Column("sequencing_depth", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "asvs",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("target_type", sa.String(length=100), nullable=True),
        sa.Column("species_name", sa.String(length=255), nullable=True),
        sa.Column("relative_abundance", sa.Numeric(precision=12, scale=8), nullable=True),
        sa.Column("length_bp", sa.Integer(), nullable=True),
        sa.Column("confidence", sa.Numeric(precision=5, scale=4), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("read_count", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "samplings",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("sample_id", sa.Integer(), nullable=False),
        sa.Column("sample_count", sa.Integer(), nullable=True),
        sa.Column("ant_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["sample_id"], ["samples.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["ant_id"], ["organisms.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_samplings_sample_id", "samplings", ["sample_id"], unique=False)
    op.create_index("ix_samplings_ant_id", "samplings", ["ant_id"], unique=False)

    op.create_table(
        "sample_confections",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("sample_id", sa.Integer(), nullable=True),
        sa.Column("organism_id", sa.Integer(), nullable=True),
        sa.Column("organism_count", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["sample_id"], ["samples.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["organism_id"], ["organisms.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_sample_confections_sample_id", "sample_confections", ["sample_id"], unique=False)
    op.create_index("ix_sample_confections_organism_id", "sample_confections", ["organism_id"], unique=False)

    op.create_table(
        "literature_references",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("sample_id", sa.Integer(), nullable=False),
        sa.Column("literature_id", sa.Integer(), nullable=False),
        sa.Column("literature_count", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["sample_id"], ["samples.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["literature_id"], ["literature.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_literature_references_sample_id", "literature_references", ["sample_id"], unique=False)
    op.create_index("ix_literature_references_literature_id", "literature_references", ["literature_id"], unique=False)

    op.create_table(
        "asv_sets",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("sequencing_run_id", sa.Integer(), nullable=False),
        sa.Column("asv_id", sa.Integer(), nullable=False),
        sa.Column("asv_count", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["sequencing_run_id"], ["sequencing_runs.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["asv_id"], ["asvs.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_asv_sets_sequencing_run_id", "asv_sets", ["sequencing_run_id"], unique=False)
    op.create_index("ix_asv_sets_asv_id", "asv_sets", ["asv_id"], unique=False)

    op.add_column("nucleotide_sequences", sa.Column("nucleotide_chain", sa.Text(), nullable=True))
    op.add_column("protein_sequences", sa.Column("protein_sequence", sa.Text(), nullable=True))

    # Preserve existing subtype rows by creating matching parent Sequence rows.
    op.execute(
        "INSERT INTO sequences (id) "
        "SELECT n.id FROM nucleotide_sequences AS n "
        "WHERE NOT EXISTS (SELECT 1 FROM sequences AS s WHERE s.id = n.id)"
    )
    op.execute(
        "INSERT INTO sequences (id) "
        "SELECT p.id FROM protein_sequences AS p "
        "WHERE NOT EXISTS (SELECT 1 FROM sequences AS s WHERE s.id = p.id)"
    )

    op.drop_index("ix_nucleotide_sequences_id", table_name="nucleotide_sequences")
    op.drop_index("ix_protein_sequences_id", table_name="protein_sequences")
    op.alter_column(
        "nucleotide_sequences",
        "id",
        existing_type=sa.Integer(),
        existing_nullable=False,
        existing_autoincrement=True,
        autoincrement=False,
    )
    op.alter_column(
        "protein_sequences",
        "id",
        existing_type=sa.Integer(),
        existing_nullable=False,
        existing_autoincrement=True,
        autoincrement=False,
    )
    op.create_foreign_key(
        "fk_nucleotide_sequences_id_sequences",
        "nucleotide_sequences",
        "sequences",
        ["id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_protein_sequences_id_sequences",
        "protein_sequences",
        "sequences",
        ["id"],
        ["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    op.drop_constraint("fk_protein_sequences_id_sequences", "protein_sequences", type_="foreignkey")
    op.drop_constraint("fk_nucleotide_sequences_id_sequences", "nucleotide_sequences", type_="foreignkey")
    op.alter_column(
        "protein_sequences",
        "id",
        existing_type=sa.Integer(),
        existing_nullable=False,
        existing_autoincrement=False,
        autoincrement=True,
    )
    op.alter_column(
        "nucleotide_sequences",
        "id",
        existing_type=sa.Integer(),
        existing_nullable=False,
        existing_autoincrement=False,
        autoincrement=True,
    )
    op.create_index("ix_protein_sequences_id", "protein_sequences", ["id"], unique=False)
    op.create_index("ix_nucleotide_sequences_id", "nucleotide_sequences", ["id"], unique=False)
    op.drop_column("protein_sequences", "protein_sequence")
    op.drop_column("nucleotide_sequences", "nucleotide_chain")

    op.drop_index("ix_asv_sets_asv_id", table_name="asv_sets")
    op.drop_index("ix_asv_sets_sequencing_run_id", table_name="asv_sets")
    op.drop_table("asv_sets")
    op.drop_index("ix_literature_references_literature_id", table_name="literature_references")
    op.drop_index("ix_literature_references_sample_id", table_name="literature_references")
    op.drop_table("literature_references")
    op.drop_index("ix_sample_confections_organism_id", table_name="sample_confections")
    op.drop_index("ix_sample_confections_sample_id", table_name="sample_confections")
    op.drop_table("sample_confections")
    op.drop_index("ix_samplings_ant_id", table_name="samplings")
    op.drop_index("ix_samplings_sample_id", table_name="samplings")
    op.drop_table("samplings")
    op.drop_table("asvs")
    op.drop_table("sequencing_runs")
    op.drop_table("sequences")
    op.drop_table("literature")
    op.drop_index("ix_samples_organism_id", table_name="samples")
    op.drop_table("samples")
