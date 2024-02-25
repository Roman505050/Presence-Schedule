from abc import ABC, abstractmethod

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

class AbstractRepository(ABC):
    @abstractmethod
    async def get_all():
        return NotImplemented
    
    @abstractmethod
    async def get_one():
        return NotImplemented
    
    @abstractmethod
    async def add_one():
        return NotImplemented

class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(stmt)
        res = result.scalars().all()
        return res
    
    async def get_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = res.scalars().first()
        if res is not None:
            return res
        return None

    async def add_one(self, kwargs: dict):
        stmt = insert(self.model).values(kwargs).returning('*')
        res = await self.session.execute(stmt)
        return res.fetchone()