from typing import Annotated
from fastapi import APIRouter, Path
from app.schemas.waterquality import Waterquality, WaterqualityCreate, WaterqualityUpdate
from app.services.waterquality import WaterqualityServiceDep
import asyncio
from fastapi import Query
# import json

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


# @router.get('/waterquality/')
# async def get_waterquality(
#     waterquality_service: WaterqualityServiceDep,
#     latitude: float = None,
#     longitude: float = None,
# ) -> list[Waterquality]:
#     filters = {}
#     if latitude is not None and longitude is not None:
#         filters["latitude"] = latitude
#         filters["longitude"] = longitude
#     return await waterquality_service.read_many(**filters)



# active_connections = []

# @router.websocket("/ws/waterquality/")
# async def websocket_endpoint(websocket: WebSocket, waterquality_service: WaterqualityServiceDep):
#     await websocket.accept()
#     active_connections.append(websocket)
#     try:
#         while True:
#             waterquality_data = await waterquality_service.read_many()
#             data_json = [data.model_dump() for data in waterquality_data]
#             await websocket.send_text(json.dumps(data_json))
#             await asyncio.sleep(5)  # обновление каждые 5 секунд
#     except WebSocketDisconnect:
#         print("WebSocket отключен")
#         active_connections.remove(websocket)


# import folium
# from fastapi.responses import HTMLResponse

# @router.get('/waterquality/map/', response_class=HTMLResponse)
# async def get_waterquality_map(
#     waterquality_service: WaterqualityServiceDep,
# ):
#     # Получаем данные о качестве воды
#     waterquality_data = await waterquality_service.read_many()

#     # Создаем карту с центром на первом объекте
#     if waterquality_data:
#         first_point = waterquality_data[0]
#         m = folium.Map(location=[first_point.latitude, first_point.longitude], zoom_start=10)
#     else:
#         m = folium.Map(location=[0, 0], zoom_start=2)

#     # Добавляем маркеры для каждого объекта
#     for data in waterquality_data:
#         folium.Marker(
#             location=[data.latitude, data.longitude],
#             popup=f"pH: {data.ph}, DO: {data.do}, Nitrates: {data.nitrates}, Phosphates: {data.phosphates}",
#             tooltip=data.model
#         ).add_to(m)

#     # Возвращаем HTML-код карты
#     return m._repr_html_()

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