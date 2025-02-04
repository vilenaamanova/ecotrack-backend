from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float
from .base import Base

class Waterquality(Base):
    __tablename__ = "waterquality"

    waterquality_code: Mapped[str] = mapped_column(String, primary_key=True)
    model: Mapped[str] = mapped_column(String, nullable=False)
    # range: Mapped[int] = mapped_column(Integer, nullable=False)
    ph: Mapped[float] = mapped_column(Float, nullable=False)
    do: Mapped[float] = mapped_column(Float, nullable=False)
    nitrates: Mapped[float] = mapped_column(Float, nullable=False)
    phosphates: Mapped[float] = mapped_column(Float, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
