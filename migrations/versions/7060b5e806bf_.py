"""empty message

Revision ID: 7060b5e806bf
Revises: 
Create Date: 2018-06-20 19:49:35.535008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7060b5e806bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop',
    sa.Column('sid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('expiration_date', sa.String(length=64), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('sid'),
    sa.UniqueConstraint('expiration_date')
    )
    op.create_index(op.f('ix_shop_name'), 'shop', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_shop_name'), table_name='shop')
    op.drop_table('shop')
    # ### end Alembic commands ###
