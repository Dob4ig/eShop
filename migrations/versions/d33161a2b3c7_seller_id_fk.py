"""seller_id FK

Revision ID: d33161a2b3c7
Revises: 442d0b3a7a54
Create Date: 2023-03-10 17:41:42.874798

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'd33161a2b3c7'
down_revision = '442d0b3a7a54'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'product', 'user', ['seller_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='foreignkey')
    # ### end Alembic commands ###
