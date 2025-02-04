# from datetime import datetime
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import func

# class Base(DeclarativeBase):
#     created_at: Mapped[datetime] = mapped_column(server_default=func.now())
#     updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, DateTime, func
from datetime import datetime
# import uuid

# class Base_Airquality(DeclarativeBase): pass

class Base(DeclarativeBase):
    # airquality_code: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

# class BaseWithId(Base):
#     __abstract__ = True
#     id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))

# from datetime import datetime
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import func
# from sqlalchemy.dialects.postgresql import UUID
# import uuid

# class Base(DeclarativeBase):
#     """
#     Базовая модель SQLAlchemy.
#     - Добавляет поля created_at и updated_at.
#     """
#     created_at: Mapped[datetime] = mapped_column(server_default=func.now())
#     updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

# class BaseWithId(Base):
#     """
#     Базовая модель с автоматически генерируемым UUID.
#     - Поле id генерируется автоматически с помощью uuid.uuid4().
#     """
#     __abstract__ = True  # Указываем, что это абстрактная модель
#     id: Mapped[str] = mapped_column(
#         UUID(as_uuid=True),  # Используем UUID тип для PostgreSQL
#         primary_key=True,
#         default=uuid.uuid4,  # Автоматически генерируем UUID
#         unique=True,
#         nullable=False,
#     )

