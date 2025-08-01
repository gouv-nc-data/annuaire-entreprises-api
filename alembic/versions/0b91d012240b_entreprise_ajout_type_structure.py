"""entreprise: ajout type structure

Revision ID: 0b91d012240b
Revises: 9e530d2bab21
Create Date: 2025-07-17 15:49:42.545850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b91d012240b'
down_revision: Union[str, None] = '9e530d2bab21'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entreprise', sa.Column('type_sctucture', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('entreprise', 'type_sctucture')
    # ### end Alembic commands ###
