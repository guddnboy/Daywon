"""Added profile image to users

Revision ID: 49a8927d3cc3
Revises: 
Create Date: 2024-05-17 00:12:46.511438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49a8927d3cc3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ranking', sa.Column('ranking_position', sa.Integer(), nullable=True))

    # Direct SQL execution to use the USING clause
    op.execute('ALTER TABLE ranking ALTER COLUMN user_point TYPE INTEGER USING user_point::integer')

    op.create_index(op.f('ix_ranking_ranking_position'), 'ranking', ['ranking_position'], unique=False)

    # Direct SQL execution to use the USING clause
    op.execute('ALTER TABLE users ALTER COLUMN user_point TYPE INTEGER USING user_point::integer')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # Direct SQL execution to revert the column type change
    op.execute('ALTER TABLE users ALTER COLUMN user_point TYPE VARCHAR USING user_point::varchar')

    op.drop_index(op.f('ix_ranking_ranking_position'), table_name='ranking')

    # Direct SQL execution to revert the column type change
    op.execute('ALTER TABLE ranking ALTER COLUMN user_point TYPE VARCHAR USING user_point::varchar')

    op.drop_column('ranking', 'ranking_position')
    # ### end Alembic commands ###
