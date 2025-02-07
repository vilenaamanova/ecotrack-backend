from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class WeatherAirQuality(Base):
    __tablename__ = "weather"
    
    id: Mapped[str] = mapped_column(Integer, primary_key=True, index=True) 
    location: Mapped[str] = mapped_column(String, index=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime)
    precipitation: Mapped[str] = mapped_column(String)
    pr_description: Mapped[str] = mapped_column(String)
    temp: Mapped[float] = mapped_column(Float)
    feels_like: Mapped[float] = mapped_column(Float)
    pressure: Mapped[int] = mapped_column(Integer)
    humidity: Mapped[int] = mapped_column(Integer)
    visibility: Mapped[int] = mapped_column(Integer)
    wind_speed: Mapped[float] = mapped_column(Float)
    clouds: Mapped[int] = mapped_column(Integer)
    country: Mapped[str] = mapped_column(String)
    city: Mapped[str] = mapped_column(String)
    aqi: Mapped[int] = mapped_column(Integer)
    co: Mapped[float] = mapped_column(Float)
    no: Mapped[float] = mapped_column(Float)
    no2: Mapped[float] = mapped_column(Float)
    o3: Mapped[float] = mapped_column(Float)
    pm10: Mapped[float] = mapped_column(Float)
    pm25: Mapped[float] = mapped_column(Float)
    so2: Mapped[float] = mapped_column(Float)
    nh3: Mapped[float] = mapped_column(Float)
