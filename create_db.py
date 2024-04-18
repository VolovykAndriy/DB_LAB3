from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:Rthj76bn@localhost/postgres")

with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE weather_db"))

print("Database 'weather_db' created successfully!")