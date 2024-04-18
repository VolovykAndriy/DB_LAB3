from datetime import datetime, timedelta

from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session
from models import WeatherData, SkyEvents

engine = create_engine("postgresql://postgres:Rthj76bn@localhost/weather_db")
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_weather_data(country: str, date: str) -> list:
    date += " 00:00:00"
    db: Session = SessionLocal()
    start_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    end_date = start_date + timedelta(hours=24)
    data = db.query(WeatherData, SkyEvents).join(SkyEvents).filter(WeatherData.country == country,
                                                                   WeatherData.last_updated >= start_date,
                                                                   WeatherData.last_updated < end_date).all()
    db.close()
    return data


# Приклад використання
if __name__ == "__main__":
    weather_data = get_weather_data("Afghanistan", "2023-08-29")
    for weather, sky_event in weather_data:
        print(f"Країна: {weather.country}")
        print(f"Дата: {weather.last_updated}")
        print(f"Схід сонця: {sky_event.sunrise}")
        print(f"Захід сонця: {sky_event.sunset}")
        print(f"Схід місяця: {sky_event.moonrise}")
        print(f"Захід місяця: {sky_event.moonset}")
        print(f"Фаза місяця: {sky_event.moon_phase}")
        print(f"Світимість місяця: {sky_event.moon_illumination}")
        print(f"Чи можливо було зустріти вервольфа: {sky_event.is_werewolf_possible}")
