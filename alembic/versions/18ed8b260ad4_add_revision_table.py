"""add revision table

Revision ID: 18ed8b260ad4
Revises: 991d469597a2
Create Date: 2022-08-24 19:11:02.079223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18ed8b260ad4'
down_revision = '991d469597a2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), sa.Column('email', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False), sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))

    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
