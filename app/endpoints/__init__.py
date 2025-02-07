from fastapi import APIRouter
from .v1 import airquality, waterquality, map_leafet

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(airquality.router)
v1_router.include_router(waterquality.router)
v1_router.include_router(map_leafet.router)
