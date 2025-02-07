from app.entities.airquality import WeatherAirQuality as AirqualityEntity
from app.schemas.airquality import WeatherAirQuality, WeatherAirQualityCreate
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.repo.session import SessionDep
from fastapi import Depends
import httpx


class AirqualityService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
    
    async def create_weather_air_quality(self, item: WeatherAirQualityCreate) -> WeatherAirQuality:
        airquality = AirqualityEntity(**item.model_dump())
        self.session.add(airquality)
        await self.session.flush()
        return WeatherAirQuality.model_validate(airquality, from_attributes=True)

    async def get_weather_air_quality(self, skip: int = 0, limit: int = 100):
        stmt = select(AirqualityEntity)
        result = await self.session.execute(stmt)
        return [WeatherAirQuality.model_validate(data, from_attributes=True) for data in result.scalars().all()]

    async def fetch_weather_data(self, lat: float, lon: float, api_key: str):
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": api_key
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch weather data: {response.status_code}")

    async def fetch_air_quality_data(self, lat: float, lon: float, api_key: str):
        url = "http://api.openweathermap.org/data/2.5/air_pollution"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": api_key
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch air quality data: {response.status_code}")


async def get_airquality_service(session: SessionDep):
    yield AirqualityService(session)

AirqualityServiceDep = Annotated[AirqualityService, Depends(get_airquality_service)]
