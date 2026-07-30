"""drop content column from posts table

Revision ID: c2_drop_content_from_posts
Revises: ad6acc46ced9
Create Date: 2026-07-31 05:10:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2_drop_content_from_posts'
down_revision: Union[str, Sequence[str], None] = 'ad6acc46ced9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_column('posts', 'content')


def downgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))