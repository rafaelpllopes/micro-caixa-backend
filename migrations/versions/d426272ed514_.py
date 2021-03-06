"""empty message

Revision ID: d426272ed514
Revises: aac5c9b25d0a
Create Date: 2021-07-24 08:23:33.256162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd426272ed514'
down_revision = 'aac5c9b25d0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('produto', 'imagem',
               existing_type=sa.TEXT(),
               nullable=True)
    op.drop_column('produto', 'qtd')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('qtd', sa.INTEGER(), autoincrement=False, nullable=True))
    op.alter_column('produto', 'imagem',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###
