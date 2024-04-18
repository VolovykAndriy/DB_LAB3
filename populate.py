import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("postgresql://postgres:Rthj76bn@localhost/weather_db")

# Прочитайте CSV-файл в DataFrame
df = pd.read_csv('GlobalWeatherRepository.csv')

df['moonrise'] = df['moonrise'].replace('No moonrise', pd.NA)
df['moonset'] = df['moonset'].replace('No moonset', pd.NA)


weather_data_df = df[['country', 'wind_degree', 'wind_kph', 'wind_direction', 'last_updated', 'sunrise', 'sunset', 'moonrise', 'moonset', 'moon_phase', 'moon_illumination']]
weather_data_df.to_sql('weather_data', engine, if_exists='append', index=False)