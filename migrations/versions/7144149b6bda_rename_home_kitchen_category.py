"""rename home_kitchen category

Revision ID: 7144149b6bda
Revises: 12d1018e21a9
Create Date: 2026-08-13 08:51:57.931203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7144149b6bda'
down_revision = '12d1018e21a9'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        UPDATE products
        SET category = 'home-kitchen'
        WHERE category = 'home_kitchen';
    """)


def downgrade():
    op.execute("""
        UPDATE products
        SET category = 'home_kitchen'
        WHERE category = 'home-kitchen';
    """)
