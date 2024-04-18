"""add_is_outdoor_safe_column

Revision ID: d21fd59abd61
Revises: a5447dbf07ca
Create Date: 2024-04-17 15:18:00.839730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd21fd59abd61'
down_revision: Union[str, None] = 'a5447dbf07ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('sky_events', sa.Column('is_werewolf_possible', sa.Boolean))

    op.execute(
        """
        UPDATE sky_events
        SET is_werewolf_possible = CASE
            WHEN moon_phase = 'Full Moon' THEN True
            ELSE False
        END;
        """
    )


def downgrade() -> None:
    op.drop_column('sky_events', 'is_werewolf_possible')
