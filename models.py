from sqlalchemy import Column, Integer, String, Float, DateTime, Time, Enum, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    country = Column(String)
    wind_degree = Column(Integer)
    wind_kph = Column(Float)
    wind_direction = Column(String)
    last_updated = Column(DateTime)


class SkyEvents(Base):
    __tablename__ = 'sky_events'
    id = Column(Integer, primary_key=True)
    weather_data_id = Column(Integer, ForeignKey('weather_data.id'))
    sunrise = Column(Time)
    sunset = Column(Time)
    moonrise = Column(Time)
    moonset = Column(Time)
    moon_phase = Column(String)
    moon_illumination = Column(Float)
    is_werewolf_possible = Column(Boolean)
