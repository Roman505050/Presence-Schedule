from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import settings


async_engine = create_async_engine(
    url=settings.db_uri_asyncpg,
    echo=True,
)
async_session_maker = async_sessionmaker(async_engine)