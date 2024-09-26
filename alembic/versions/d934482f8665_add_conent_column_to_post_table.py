"""add conent column to post table

Revision ID: d934482f8665
Revises: 23e2117944ac
Create Date: 2024-09-26 20:11:08.232642

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd934482f8665'
down_revision: Union[str, None] = '23e2117944ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
