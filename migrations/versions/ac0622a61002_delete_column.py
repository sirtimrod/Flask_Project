"""Delete column

Revision ID: ac0622a61002
Revises: e2b326623f08
Create Date: 2021-10-27 15:14:18.934793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac0622a61002'
down_revision = 'cb8434c45b50'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('pages', 'country_code')


def downgrade():
    op.add_column('pages', sa.Column('country_code', sa.String(), nullable=True))
