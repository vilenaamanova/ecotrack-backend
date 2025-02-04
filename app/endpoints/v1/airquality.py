from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from fastapi import HTTPException
import os
from datetime import datetime
from app.services.airquality import AirqualityServiceDep

router = APIRouter(tags=['Airquality'])


from app.schemas.airquality import WeatherAirQuality, WeatherAirQualityCreate
# from app.services import airquality as crud
import requests

@router.post("/weather-air-quality/")
async def create_weather_air_quality(
    airquality_service: AirqualityServiceDep,
    data: WeatherAirQualityCreate,
) -> WeatherAirQuality:
    return await airquality_service.create_weather_air_quality(data)

@router.get("/weather-air-quality/")
async def read_weather_air_quality(
    airquality_service: AirqualityServiceDep,
    skip: int = 0, 
    limit: int = 100, 
    ) -> list[WeatherAirQuality]:
    return await airquality_service.get_weather_air_quality(skip=skip, limit=limit)


@router.get("/fetch-weather-air-quality/")
async def fetch_and_save_weather_air_quality(
    lat: float, # Annotated[float, Path(title="Latitude of airquality")
    lon: float,
    airquality_service: AirqualityServiceDep,
    ):
    try:
        api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        weather_data = await airquality_service.fetch_weather_data(lat, lon, api_key)
        air_pollution_data = await airquality_service.fetch_air_quality_data(lat, lon, api_key)
        if not weather_data or not air_pollution_data:
            raise HTTPException(status_code=500, detail="Failed to fetch valid data from APIs")
        # Сохраняем данные в базу данных
        weather_air_quality = WeatherAirQualityCreate(
            location=f"Lat: {lat}, Lon {lon}",
            timestamp=datetime.now().replace(tzinfo=None),
            precipitation=weather_data["weather"][0]["main"],
            pr_description=weather_data["weather"][0]["description"],
            temp=weather_data["main"]["temp"],
            feels_like=weather_data["main"]["feels_like"],
            pressure=weather_data["main"]["pressure"],
            humidity=weather_data["main"]["humidity"],
            visibility=weather_data["visibility"],
            wind_speed=weather_data["wind"]["speed"],
            clouds=weather_data["clouds"]["all"],
            country=weather_data["sys"]["country"],
            city=weather_data["name"],
            aqi=air_pollution_data["list"][0]["main"]["aqi"],
            co=air_pollution_data["list"][0]["components"]["co"],
            no=air_pollution_data["list"][0]["components"]["no"],
            no2=air_pollution_data["list"][0]["components"]["no2"],
            o3=air_pollution_data["list"][0]["components"]["o3"],
            pm10=air_pollution_data["list"][0]["components"]["pm10"],
            pm25=air_pollution_data["list"][0]["components"]["pm2_5"],
            so2=air_pollution_data["list"][0]["components"]["so2"],
            nh3=air_pollution_data["list"][0]["components"]["nh3"]
        )
        await airquality_service.create_weather_air_quality(weather_air_quality)

        return {"message": "Weather and air quality data fetched and saved successfully"}
    except requests.exceptions.RequestException as e:
        # Ловим ошибки, если запрос к API не удался
        raise HTTPException(status_code=500, detail=f"Error with API request: {str(e)}")
    
    except Exception as e:
        # Обрабатываем любые другие ошибки
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")