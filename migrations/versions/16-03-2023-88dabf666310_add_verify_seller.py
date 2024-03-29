"""add verify seller

Revision ID: 88dabf666310
Revises: d33161a2b3c7
Create Date: 2023-03-16 00:41:24.106638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88dabf666310'
down_revision = 'd33161a2b3c7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('verify_quee',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('shop_name', sa.String(
                        length=50), nullable=False),
                    sa.Column('description', sa.Text(), nullable=False),
                    sa.Column('image_path', sa.String(100), nullable=True),
                    sa.Column('owner_id', sa.Integer(), nullable=False),
                    sa.Column('added_at', sa.TIMESTAMP(), nullable=False),
                    sa.ForeignKeyConstraint(['owner_id'], ['product.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.alter_column('product', 'seller_id',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'seller_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.drop_table('verify_quee')
    # ### end Alembic commands ###
