"""Create initial tables

Revision ID: 6efc0900b250
Revises: 
Create Date: 2024-04-17 14:57:32.313944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6efc0900b250'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'weather_data',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('country', sa.String),
        sa.Column('wind_degree', sa.Integer),
        sa.Column('wind_kph', sa.Float),
        sa.Column('wind_direction', sa.String),
        sa.Column('last_updated', sa.DateTime),
        sa.Column('sunrise', sa.Time),
        sa.Column('sunset', sa.Time),
        sa.Column('moonrise', sa.Time),
        sa.Column('moonset', sa.Time),
        sa.Column('moon_phase', sa.String),
        sa.Column('moon_illumination', sa.Float)
    )


def downgrade() -> None:
    op.drop_table('weather_data')
