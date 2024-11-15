"""created add added to sp

Revision ID: adb48500e6d4
Revises: 46ebbb96b60a
Create Date: 2024-11-15 00:01:34.190492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adb48500e6d4'
down_revision = '46ebbb96b60a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('store_products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('store_products', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###