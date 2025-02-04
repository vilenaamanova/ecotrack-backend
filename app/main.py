from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.repo.session import engine, make_session, test_conn, get_session
from app.endpoints import v1_router
from app.entities.base import Base

from app import entities
from faker import Faker
import uuid
import random

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Инициализация базы данных (например, создание таблиц)
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     yield

# @asynccontextmanager
# async def on_start(app: FastAPI):
#     async with make_session() as session:
#         async with session.begin():
#             session.add(entities.Aircraft(aircraft_code="122", model="Test", range=3))
#             await session.commit()
#     yield

faker = Faker()

# @asynccontextmanager
# async def on_start(app: FastAPI):
#     """Запускается при старте FastAPI. Записывает 100 случайных записей в таблицу."""
#     try:
#         async with make_session() as session:
#             async with session.begin():
#                 fake_airquality = [
#                     entities.Airquality(
#                         airquality_code=str(uuid.uuid4()),
#                         model=faker.word(),
#                         pm2_5=round(random.uniform(0.0, 250.0), 2),
#                         pm_10=round(random.uniform(0.0, 400.0), 2),
#                         co=round(random.uniform(0.0, 25.0), 2),
#                         no2=round(random.uniform(0.0, 400.0), 2),
#                     )
#                     for _ in range(100)
#                 ]
#                 session.add_all(fake_airquality)
#                 await session.commit()
#                 print("100 случайных записей добавлены в таблицу airquality!")
#     except Exception as e:
#         print(f"Ошибка при добавлении: {e}")
#     yield  # Позволяет продолжить выполнение FastAPI

# Kazan 55.796127, 49.106414
# Sochi 43.585472 39.723098
@asynccontextmanager
async def on_start(app: FastAPI):
    """Запускается при старте FastAPI. Записывает 100 случайных записей в таблицу."""
    try:
        async with make_session() as session:
            async with session.begin():
                fake_waterquality = [
                    entities.Waterquality(
                        waterquality_code=str(uuid.uuid4()),
                        model= str('Sochi'),
                        ph=round(random.uniform(6.0, 8.5), 2),
                        do=round(random.uniform(4.0, 10.0), 2),
                        nitrates=round(random.uniform(0.0, 20.0), 2),
                        phosphates=round(random.uniform(0.0, 2.0), 2),
                        latitude=43.585472,
                        longitude=39.723098
                    )
                    for _ in range(50)
                ]
                session.add_all(fake_waterquality)
                await session.commit()
                print("100 случайных записей добавлены в таблицу waterquality!")
    except Exception as e:
        print(f"Ошибка при добавлении: {e}")
    yield  # Позволяет продолжить выполнение FastAPI

# app = FastAPI(lifespan=on_start)

app = FastAPI()



from fastapi.middleware.cors import CORSMiddleware
# Настройка CORS, чтобы разрешить запросы с порта 8001
origins = [
    "http://localhost:8001",  # Разрешить запросы с порта 8001
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить запросы с этих источников
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP методы
    allow_headers=["*"],  # Разрешить все заголовки
)

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
# Настройка статических файлов (если нужно для стилей и JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключение роутеров
app.include_router(v1_router, prefix="/api")

@app.router.get("/waterquality/map", response_class=HTMLResponse)
async def show_map():
    with open("static/index.html", "r") as file:
        return file.read()

from app.schemas.airquality import WeatherAirQuality, WeatherAirQualityCreate
from app.services import airquality as crud
import requests

# @app.post("/weather-air-quality/", response_model=WeatherAirQualityCreate)
# def create_weather_air_quality(weather_air_quality: WeatherAirQualityCreate, db: Session = Depends(get_session)):
#     return crud.create_weather_air_quality(db, weather_air_quality)


# @app.get("/weather-air-quality/", response_model=list[WeatherAirQualityCreate])
# async def read_weather_air_quality(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
#     return await crud.get_weather_air_quality(db, skip=skip, limit=limit)


# @app.get("/fetch-weather-air-quality/")
# def fetch_and_save_weather_air_quality(lat: float, lon: float, db: Session = Depends(get_session)):
#     try:
#         weather_data = crud.fetch_weather_data(lat, lon, os.getenv("OPENWEATHERMAP_API_KEY"))
#         # print(weather_data)
#         air_pollution_data = crud.fetch_air_quality_data(lat, lon, os.getenv("OPENWEATHERMAP_API_KEY"))
#         if not weather_data or not air_pollution_data:
#             raise HTTPException(status_code=500, detail="Failed to fetch valid data from APIs")
#         # Сохраняем данные в базу данных
#         weather_air_quality = WeatherAirQualityCreate(
#             location=f"Lat: {lat}, Lon {lon}",
#             timestamp=datetime.now(),
#             precipitation=weather_data["weather"][0]["main"],
#             pr_description=weather_data["weather"][0]["description"],
#             temp=weather_data["main"]["temp"],
#             feels_like=weather_data["main"]["feels_like"],
#             pressure=weather_data["main"]["pressure"],
#             humidity=weather_data["main"]["humidity"],
#             visibility=weather_data["visibility"],
#             wind_speed=weather_data["wind"]["speed"],
#             clouds=weather_data["clouds"]["all"],
#             country=weather_data["sys"]["country"],
#             city=weather_data["name"],
#             aqi=air_pollution_data["list"][0]["main"]["aqi"],
#             co=air_pollution_data["list"][0]["components"]["co"],
#             no=air_pollution_data["list"][0]["components"]["no"],
#             no2=air_pollution_data["list"][0]["components"]["no2"],
#             o3=air_pollution_data["list"][0]["components"]["o3"],
#             pm10=air_pollution_data["list"][0]["components"]["pm10"],
#             pm25=air_pollution_data["list"][0]["components"]["pm2_5"],
#             so2=air_pollution_data["list"][0]["components"]["so2"],
#             nh3=air_pollution_data["list"][0]["components"]["nh3"]
#         )
#         crud.create_weather_air_quality(db, weather_air_quality)

#         return {"message": "Weather and air quality data fetched and saved successfully"}
#     except requests.exceptions.RequestException as e:
#         # Ловим ошибки, если запрос к API не удался
#         raise HTTPException(status_code=500, detail=f"Error with API request: {str(e)}")
    
#     except Exception as e:
#         # Обрабатываем любые другие ошибки
#         raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
    
# @app.get('/health')
# async def get_health() -> dict:
#     return {"status": "OK"}