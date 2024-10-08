"""model postagem criada

Revision ID: 2c80b79570dd
Revises: d333771b2503
Create Date: 2024-09-21 10:06:15.790850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c80b79570dd'
down_revision: Union[str, None] = 'd333771b2503'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_postagens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('perfil_id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=200), nullable=False),
    sa.Column('texto', sa.Text(), nullable=False),
    sa.Column('data_hora', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['perfil_id'], ['tb_perfis.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_postagens')
    # ### end Alembic commands ###
