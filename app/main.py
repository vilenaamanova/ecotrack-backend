from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.repo.session import engine, make_session, test_conn, get_session
from app.endpoints import v1_router

from app import entities
from faker import Faker
import uuid
import random

from fastapi.responses import HTMLResponse
from dotenv import load_dotenv

from fastapi.middleware.cors import CORSMiddleware

faker = Faker()


@asynccontextmanager
async def on_start(app: FastAPI):
    try:
        async with make_session() as session:
            async with session.begin():
                fake_waterquality = [
                    entities.Waterquality(
                        waterquality_code=str(uuid.uuid4()),
                        model=str('Sochi'),
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
    yield

app = FastAPI()

origins = [
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

app.include_router(v1_router, prefix="/api")


@app.router.get("/waterquality/map", response_class=HTMLResponse)
async def show_map():
    with open("static/index.html", "r") as file:
        return file.read()
