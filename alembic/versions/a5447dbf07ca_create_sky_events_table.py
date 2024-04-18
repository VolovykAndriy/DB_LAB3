"""create_sky_events_table

Revision ID: a5447dbf07ca
Revises: 6efc0900b250
Create Date: 2024-04-17 15:17:45.100601

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'a5447dbf07ca'
down_revision: Union[str, None] = '6efc0900b250'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'sky_events',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('weather_data_id', sa.Integer, sa.ForeignKey('weather_data.id')),
        sa.Column('sunrise', sa.Time),
        sa.Column('sunset', sa.Time),
        sa.Column('moonrise', sa.Time),
        sa.Column('moonset', sa.Time),
        sa.Column('moon_phase', sa.String),
        sa.Column('moon_illumination', sa.Float),
    )

    op.execute(
        """
        INSERT INTO sky_events (weather_data_id, sunrise, sunset, moonrise, moonset, moon_phase, moon_illumination)
        SELECT id, sunrise, sunset, moonrise, moonset, moon_phase, moon_illumination
        FROM weather_data;
        """
    )

    op.drop_column('weather_data', 'sunrise')
    op.drop_column('weather_data', 'sunset')
    op.drop_column('weather_data', 'moonrise')
    op.drop_column('weather_data', 'moonset')
    op.drop_column('weather_data', 'moon_phase')
    op.drop_column('weather_data', 'moon_illumination')


def downgrade() -> None:
    op.add_column('weather_data', sa.Column('sunrise', sa.Time))
    op.add_column('weather_data', sa.Column('sunset', sa.Time))
    op.add_column('weather_data', sa.Column('moonrise', sa.Time))
    op.add_column('weather_data', sa.Column('moonset', sa.Time))
    op.add_column('weather_data', sa.Column('moon_phase', sa.String))
    op.add_column('weather_data', sa.Column('moon_illumination', sa.Float))

    op.execute(
        """
        UPDATE weather_data
        SET sunrise = sky_events.sunrise,
            sunset = sky_events.sunset,
            moonrise = sky_events.moonrise,
            moonset = sky_events.moonset,
            moon_phase = sky_events.moon_phase,
            moon_illumination = sky_events.moon_illumination
        FROM sky_events
        WHERE weather_data.id = sky_events.weather_data_id;
        """
    )

    op.drop_table('sky_events')
