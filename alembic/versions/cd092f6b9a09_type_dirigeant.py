"""type dirigeant

Revision ID: cd092f6b9a09
Revises: 44a1c08b69ed
Create Date: 2025-01-13 09:01:43.473347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd092f6b9a09'
down_revision: Union[str, None] = '44a1c08b69ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dirigeant', sa.Column('type_personne', sa.String(), nullable=True))
    op.add_column('dirigeant', sa.Column('ordreaffichage', sa.Integer(), nullable=True))
    op.add_column('dirigeant', sa.Column('numerochrono', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dirigeant', 'numerochrono')
    op.drop_column('dirigeant', 'ordreaffichage')
    op.drop_column('dirigeant', 'type_personne')
    # ### end Alembic commands ###