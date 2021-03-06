"""empty message

Revision ID: 213e071c6ee0
Revises: d4e7caaff770
Create Date: 2021-07-24 07:15:04.449628

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '213e071c6ee0'
down_revision = 'd4e7caaff770'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carrinho',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('venda', sa.Integer(), nullable=False),
    sa.Column('produto', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.Column('criado', sa.DateTime(timezone=6), nullable=False),
    sa.Column('atualizado', sa.DateTime(timezone=6), nullable=False),
    sa.ForeignKeyConstraint(['produto'], ['produto.id'], ),
    sa.ForeignKeyConstraint(['venda'], ['venda.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('venda', sa.Column('criado', sa.DateTime(timezone=6), nullable=False))
    op.add_column('venda', sa.Column('atualizado', sa.DateTime(timezone=6), nullable=False))
    op.drop_constraint('venda_item_fkey', 'venda', type_='foreignkey')
    op.drop_column('venda', 'data_hora')
    op.drop_column('venda', 'quantidade')
    op.drop_column('venda', 'item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venda', sa.Column('item', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('venda', sa.Column('quantidade', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('venda', sa.Column('data_hora', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False))
    op.create_foreign_key('venda_item_fkey', 'venda', 'produto', ['item'], ['id'])
    op.drop_column('venda', 'atualizado')
    op.drop_column('venda', 'criado')
    op.drop_table('carrinho')
    # ### end Alembic commands ###
