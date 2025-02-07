from typing import Annotated, AsyncGenerator
from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

engine = create_async_engine("postgresql+asyncpg://admin:admin@localhost:5433/database", echo=True)
make_session = async_sessionmaker(engine)


async def test_conn():
    async with make_session() as session:
        async with session.begin():
            try:
                result = await session.execute(text("select 'hello world'"))
                print(f'{result.scalar()=}')
            finally:
                await session.close()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session = make_session()
    try:
        session.begin()
        yield session
    finally:
        await session.commit()
        await session.close()


SessionDep = Annotated[AsyncSession, Depends(get_session)]
