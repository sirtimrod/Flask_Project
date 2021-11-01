"""Test migration

Revision ID: e2b326623f08
Revises: cb8434c45b50
Create Date: 2021-10-27 11:13:38.759353

"""
from alembic import op
import sqlalchemy as sa

import ipapi

# revision identifiers, used by Alembic.
revision = 'e2b326623f08'
down_revision = 'cb8434c45b50'
branch_labels = None
depends_on = None


def sql_update(conn):

    db_data = conn.execute('SELECT id, external_ip FROM pages')
    results = db_data.fetchall()

    for res in results:
        conn.execute(f"UPDATE pages SET country_code = '{ipapi.location(ip=res[1], output='country')}'"
                     f"WHERE id = {int(res[0])}")


def upgrade():

    op.add_column('pages', sa.Column('country_code', sa.String(), nullable=False, server_default='CODE'))

    conn = op.get_bind()
    sql_update(conn)


def downgrade():
    op.drop_column('pages', 'country_code')
