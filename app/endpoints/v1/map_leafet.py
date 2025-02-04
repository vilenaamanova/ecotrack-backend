from app.services.waterquality import WaterqualityServiceDep
from fastapi import APIRouter

router = APIRouter(tags=['mapWaterquality'])

@router.get('/waterquality/map/')
async def get_waterquality_map(
    waterquality_service: WaterqualityServiceDep,
) -> list[dict]:
    # Получаем все данные для отображения на карте
    waterquality_data = await waterquality_service.read_many()

    # Формируем данные в формате, который будет использован на карте
    map_data = [
        {
            "waterquality_code": item.waterquality_code,
            "model": item.model,
            "ph": item.ph,
            "do": item.do,
            "nitrates": item.nitrates,
            "phosphates": item.phosphates,
            "latitude": item.latitude,
            "longitude": item.longitude
        }
        for item in waterquality_data
    ]
    return map_data
