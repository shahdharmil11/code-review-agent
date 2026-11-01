"""create patterns table

Revision ID: 0003
Revises: 0002
Create Date: 2026-11-01 00:20:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0003"
down_revision: Union[str, None] = "0002"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "patterns",
        sa.Column("id", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("repo_full_name", sa.Text(), nullable=False),
        sa.Column("pattern_text", sa.Text(), nullable=False),
        sa.Column("frequency", sa.Integer(), server_default="1", nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("repo_full_name", "pattern_text"),
    )


def downgrade() -> None:
    op.drop_table("patterns")
