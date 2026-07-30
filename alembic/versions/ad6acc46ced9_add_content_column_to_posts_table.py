"""add content column to posts table

Revision ID: ad6acc46ced9
Revises: a034632bce41
Create Date: 2026-07-31 04:49:08.438220

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad6acc46ced9'
down_revision: Union[str, Sequence[str], None] = 'a034632bce41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # use IF NOT EXISTS to avoid duplicate-column errors when the column
    # is already present (it was added in another migration file)
    op.execute("ALTER TABLE posts ADD COLUMN IF NOT EXISTS content VARCHAR")
    # ensure NOT NULL if desired; uncomment if safe:
    # op.execute("ALTER TABLE posts ALTER COLUMN content SET NOT NULL")
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
