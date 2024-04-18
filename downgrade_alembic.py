from alembic.config import Config
from alembic import command

alembic_cfg = Config("alembic.ini")

# command.downgrade(alembic_cfg, "d21fd59abd61")
# command.downgrade(alembic_cfg, "a5447dbf07ca")
command.downgrade(alembic_cfg, "6efc0900b250")
