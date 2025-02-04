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


# from sqlalchemy.orm import Mapped, mapped_column
# from .base import Base

# class Aircraft(Base):
#     __tablename__ = 'aircrafts'
#     aircraft_code: Mapped[str] = mapped_column(primary_key=True)
#     model: Mapped[str]
#     range: Mapped[int]

# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy import String, Integer, Float
# from .base import Base

# class Airquality(Base):
#     __tablename__ = "airquality"

#     airquality_code: Mapped[str] = mapped_column(String, primary_key=True)
#     model: Mapped[str] = mapped_column(String, nullable=False)
#     # range: Mapped[int] = mapped_column(Integer, nullable=False)
#     pm2_5: Mapped[float] = mapped_column(Float, nullable=False)
#     pm_10: Mapped[float] = mapped_column(Float, nullable=False)
#     co: Mapped[float] = mapped_column(Float, nullable=False)
#     no2: Mapped[float] = mapped_column(Float, nullable=False)
