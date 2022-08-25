"""add content column to posts table

Revision ID: 991d469597a2
Revises: 2bd1ce395ccb
Create Date: 2022-08-24 19:00:38.592956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '991d469597a2'
down_revision = '2bd1ce395ccb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
