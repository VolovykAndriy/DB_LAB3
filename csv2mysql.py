import pandas as pd
from sqlalchemy import create_engine, text


engine = create_engine("mysql+pymysql://MySQL:Rthj76bn@localhost/weather_db")

with engine.connect() as connection:
    connection.execute(text("DROP TABLE IF EXISTS sky_events"))
    connection.execute(text("DROP TABLE IF EXISTS weather_data"))

weather_data_df = pd.read_csv('MySQl/weather_data.csv')
sky_events_df = pd.read_csv('MySQl/sky_events.csv')

weather_data_df.to_sql('weather_data', con=engine, if_exists='append', index=False)
sky_events_df.to_sql('sky_events', con=engine, if_exists='append', index=False)
