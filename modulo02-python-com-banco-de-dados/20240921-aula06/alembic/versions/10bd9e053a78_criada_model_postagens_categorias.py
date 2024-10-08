"""criada model postagens_categorias

Revision ID: 10bd9e053a78
Revises: 2aac73d6440d
Create Date: 2024-09-21 10:38:20.646446

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10bd9e053a78'
down_revision: Union[str, None] = '2aac73d6440d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_postagens_categorias',
    sa.Column('postagem_id', sa.Integer(), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['tb_categorias.id'], ),
    sa.ForeignKeyConstraint(['postagem_id'], ['tb_postagens.id'], ),
    sa.PrimaryKeyConstraint('postagem_id', 'categoria_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_postagens_categorias')
    # ### end Alembic commands ###
