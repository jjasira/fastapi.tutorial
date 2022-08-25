"""add last few columns to post table

Revision ID: c2315cd8834b
Revises: 99a2b2efe619
Create Date: 2022-08-24 19:37:52.847159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2315cd8834b'
down_revision = '99a2b2efe619'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False),)
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default="TRUE"),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
