from pydantic import BaseModel
from .base import BaseEntitySchema


class WaterqualityBase(BaseModel):
    waterquality_code: str
    model: str
    ph: float
    do: float
    nitrates: float
    phosphates: float
    latitude: float
    longitude: float


class WaterqualityCreate(WaterqualityBase):
    pass


class WaterqualityUpdate(BaseModel):
    model: str | None = None
    ph: float | None = None
    do: float | None = None
    nitrates: float | None = None
    phosphates: float | None = None
    latitude: float | None = None
    longitude: float | None = None


class Waterquality(WaterqualityBase, BaseEntitySchema):
    pass
