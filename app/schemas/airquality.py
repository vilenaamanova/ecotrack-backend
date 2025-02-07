from pydantic import BaseModel
from datetime import datetime


class WeatherAirQualityBase(BaseModel):
    location: str
    timestamp: datetime
    precipitation: str 
    pr_description: str 
    temp: float 
    feels_like: float 
    pressure: int 
    humidity: int 
    visibility: int 
    wind_speed: float 
    clouds: int 
    country: str 
    city: str 
    aqi: int 
    co: float 
    no: float 
    no2: float 
    o3: float 
    pm10: float 
    pm25: float 
    so2: float 
    nh3: float 


class WeatherAirQualityCreate(WeatherAirQualityBase):
    pass


class WeatherAirQuality(WeatherAirQualityBase):
    id: int

    class Config:
        orm_mode = True
