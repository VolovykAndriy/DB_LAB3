from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://MySQL:Rthj76bn@localhost/weather_db")

with engine.connect() as connection:
    connection.execute(text("DROP TABLE IF EXISTS sky_events"))
    connection.execute(text("DROP TABLE IF EXISTS weather_data"))
