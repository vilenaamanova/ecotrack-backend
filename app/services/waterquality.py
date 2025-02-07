from typing import Annotated, Any
from fastapi import Depends
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.waterquality import Waterquality, WaterqualityCreate, WaterqualityUpdate
from app.repo.session import SessionDep
from app.entities.waterquality import Waterquality as WaterqualityEntity

active_connections = []


class WaterqualityService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def read_many(self, **kwargs: Any) -> list[Waterquality]:
        stmt = select(WaterqualityEntity)
        result = await self.session.execute(stmt)
        return [Waterquality.model_validate(data, from_attributes=True) for data in result.scalars().all()]

    async def read_one(self, waterquality_code: str) -> Waterquality:
        stmt = select(WaterqualityEntity).where(WaterqualityEntity.waterquality_code == waterquality_code)
        result = await self.session.execute(stmt)
        return Waterquality.model_validate(result.scalar(), from_attributes=True)

    async def create(self, item: WaterqualityCreate) -> Waterquality:
        waterquality = WaterqualityEntity(**item.model_dump())
        self.session.add(waterquality)
        await self.session.flush()
        return Waterquality.model_validate(waterquality, from_attributes=True)

    async def update(self, waterquality_code: str, item: WaterqualityUpdate) -> Waterquality:
        stmt = update(WaterqualityEntity).returning(WaterqualityEntity).where(WaterqualityEntity.waterquality_code == waterquality_code).values(**item.model_dump())
        result = await self.session.execute(stmt)
        return Waterquality.model_validate(result.scalar(), from_attributes=True)

    async def delete(self, waterquality_code: str) -> None:
        stmt = delete(WaterqualityEntity).where(WaterqualityEntity.waterquality_code == waterquality_code)
        await self.session.execute(stmt)

    async def delete_all(self, **kwargs: Any) -> None:
        stmt = delete(WaterqualityEntity)
        await self.session.execute(stmt)

    async def read_by_city(self, city: str) -> list[Waterquality]:
        stmt = select(WaterqualityEntity).filter(WaterqualityEntity.model == city)
        result = await self.session.execute(stmt)
        return [Waterquality.model_validate(data, from_attributes=True) for data in result.scalars().all()]


async def get_waterquality_service(session: SessionDep):
    yield WaterqualityService(session)

WaterqualityServiceDep = Annotated[WaterqualityService, Depends(get_waterquality_service)]
