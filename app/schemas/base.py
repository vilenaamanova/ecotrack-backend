from pydantic import BaseModel
from datetime import datetime


class BaseEntitySchema(BaseModel):
    created_at: datetime | None = None
    updated_at: datetime | None = None