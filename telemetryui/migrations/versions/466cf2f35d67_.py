"""empty message

Revision ID: 466cf2f35d67
Revises: 3230c615d6e0
Create Date: 2017-09-12 21:33:00.335130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '466cf2f35d67'
down_revision = '3230c615d6e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('records', sa.Column('bios_version', sa.String(), nullable=True))
    op.add_column('records', sa.Column('board_name', sa.String(), nullable=True))
    op.add_column('records', sa.Column('cpu_model', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('records', 'cpu_model')
    op.drop_column('records', 'board_name')
    op.drop_column('records', 'bios_version')
    # ### end Alembic commands ###
