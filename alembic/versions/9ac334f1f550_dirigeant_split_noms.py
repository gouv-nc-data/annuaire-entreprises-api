"""dirigeant split noms

Revision ID: 9ac334f1f550
Revises: 4970fc7626b7
Create Date: 2025-01-15 13:41:35.736371

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ac334f1f550'
down_revision: Union[str, None] = '4970fc7626b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dirigeant', sa.Column('prenoms', sa.String(), nullable=True))
    op.add_column('dirigeant', sa.Column('nom_personne_morale', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dirigeant', 'nom_personne_morale')
    op.drop_column('dirigeant', 'prenoms')
    # ### end Alembic commands ###