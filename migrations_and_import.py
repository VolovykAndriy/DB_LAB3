import pandas as pd
from sqlalchemy import create_engine, text
from alembic.config import Config
from alembic import command

# Настройки базы данных и пути к файлам
engine = create_engine("postgresql://postgres:Rthj76bn@localhost/weather_db")
df = pd.read_csv('GlobalWeatherRepository.csv')

df['moonrise'] = df['moonrise'].replace('No moonrise', pd.NA)
df['moonset'] = df['moonset'].replace('No moonset', pd.NA)

alembic_cfg = Config("alembic.ini")
# command.upgrade(alembic_cfg, "6efc0900b250")
#
# weather_data_df = df[['country', 'wind_degree', 'wind_kph', 'wind_direction', 'last_updated', 'sunrise', 'sunset', 'moonrise', 'moonset', 'moon_phase', 'moon_illumination']]
# weather_data_df.to_sql('weather_data', engine, if_exists='append', index=False)

# command.upgrade(alembic_cfg, "a5447dbf07ca")
command.upgrade(alembic_cfg, "d21fd59abd61")
print("Міграції даних завершено!")

