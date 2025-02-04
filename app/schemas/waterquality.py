from pydantic import BaseModel
from .base import BaseEntitySchema

class WaterqualityBase(BaseModel):
    waterquality_code: str
    model: str # модель датчика
    ph: float # pH значения в пределах норм
    do: float # Растворённый кислород в воде (DO)
    nitrates: float # Нитраты (NO3)
    phosphates: float # Фосфаты (PO4)
    latitude: float
    longitude: float
    # range: int

class WaterqualityCreate(WaterqualityBase):
    pass

class WaterqualityUpdate(BaseModel):
    model: str | None = None
    # range: int | None = None
    ph: float | None = None
    do: float | None = None
    nitrates: float | None = None
    phosphates: float | None = None
    latitude: float | None = None
    longitude: float | None = None

class Waterquality(WaterqualityBase, BaseEntitySchema):
    pass