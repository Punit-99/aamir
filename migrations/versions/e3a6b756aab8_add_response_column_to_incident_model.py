"""Add response column to Incident model

Revision ID: e3a6b756aab8
Revises: 
Create Date: 2024-06-27 18:36:08.622878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3a6b756aab8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('incident', schema=None) as batch_op:
        batch_op.add_column(sa.Column('response', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('incident', schema=None) as batch_op:
        batch_op.drop_column('response')

    # ### end Alembic commands ###
