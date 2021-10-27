"""Test migration

Revision ID: e2b326623f08
Revises: cb8434c45b50
Create Date: 2021-10-27 11:13:38.759353

"""
from alembic import op
import sqlalchemy as sa
import requests


# revision identifiers, used by Alembic.
revision = 'e2b326623f08'
down_revision = 'ac0622a61002'
branch_labels = None
depends_on = None


def get_code(external_ip):
    country_code = requests.get(f'http://api.ipstack.com/{external_ip}?'
                                f'access_key=74a3ef2e0e526908b52d42f40bd961ef').json()
    return country_code['country_code']


def upgrade():

    conn = op.get_bind()

    op.add_column('pages', sa.Column('country_code', sa.String(), nullable=True))

    db_data = conn.execute('SELECT id, external_ip FROM pages')
    results = db_data.fetchall()

    for res in results:
        conn.execute(f"UPDATE pages SET country_code = '{get_code(res[1])}' WHERE id = {int(res[0])}")


def downgrade():
    op.drop_column('pages', 'country_code')
