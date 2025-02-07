from typing import Annotated
from fastapi import APIRouter, Path
from app.schemas.waterquality import Waterquality, WaterqualityCreate, WaterqualityUpdate
from app.services.waterquality import WaterqualityServiceDep

router = APIRouter(tags=['Waterquality'])


@router.get('/waterquality/')
async def get_waterquality(
    waterquality_service: WaterqualityServiceDep,
) -> list[Waterquality]:
    return await waterquality_service.read_many()


@router.get('/waterquality/map/')
async def get_waterquality_for_map(
    waterquality_service: WaterqualityServiceDep,
) -> list[Waterquality]:
    waterquality_data = await waterquality_service.read_many()
    return [{
        'waterquality_code': item.waterquality_code,
        'model': item.model,
        'ph': item.ph,
        'do': item.do,
        'nitrates': item.nitrates,
        'phosphates': item.phosphates,
        'latitude': item.latitude,
        'longitude': item.longitude,
    } for item in waterquality_data]


@router.get('/waterquality/{waterquality_code}')
async def get_waterquality(
    waterquality_code: Annotated[str, Path(title="Code of waterquality")],
    waterquality_service: WaterqualityServiceDep
) -> Waterquality:
    return await waterquality_service.read_one(waterquality_code)


@router.post('/waterquality/')
async def create_waterquality(
    waterquality_service: WaterqualityServiceDep,
    data: WaterqualityCreate,
) -> Waterquality:
    return await waterquality_service.create(data)


@router.put('/waterquality/{waterquality_code}')
async def update_waterquality(
    waterquality_code: Annotated[str, Path(title="Code of waterquality")],
    waterquality_service: WaterqualityServiceDep,
    data: WaterqualityUpdate,
) -> Waterquality:
    return await waterquality_service.update(waterquality_code, data)


@router.delete('/waterquality/')
async def delete_all_waterquality(
    waterquality_service: WaterqualityServiceDep,
) -> None:
    await waterquality_service.delete_all()


@router.delete('/waterquality/{waterquality_code}')
async def delete_waterquality(
    waterquality_code: Annotated[str, Path(title="Code of waterquality")],
    waterquality_service: WaterqualityServiceDep,
) -> None:
    await waterquality_service.delete(waterquality_code)