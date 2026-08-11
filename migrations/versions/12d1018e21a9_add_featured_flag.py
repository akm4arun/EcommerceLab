"""add featured flag

Revision ID: 12d1018e21a9
Revises: 2d6fdebafdf2
Create Date: 2026-08-11 06:55:22.036708
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect

revision = '12d1018e21a9'
down_revision = '2d6fdebafdf2'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    inspector = inspect(bind)
    columns = [c['name'] for c in inspector.get_columns('products')]

    if 'featured' not in columns:
        op.add_column(
            'products',
            sa.Column('featured', sa.Boolean(), nullable=True)
        )


def downgrade():
    bind = op.get_bind()
    inspector = inspect(bind)
    columns = [c['name'] for c in inspector.get_columns('products')]

    if 'featured' in columns:
        op.drop_column('products', 'featured')