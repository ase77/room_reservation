"""add user relationship to Resrvation

Revision ID: 143e3081d5e9
Revises: 23f59cb3e73b
Create Date: 2022-11-09 19:58:40.379050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '143e3081d5e9'
down_revision = '23f59cb3e73b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_reservation_user_id_user', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.drop_constraint('fk_reservation_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
