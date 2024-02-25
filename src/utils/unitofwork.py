from abc import ABC, abstractmethod
from typing import Type

from src.database.core import async_session_maker
from src.repositories import ScheduleRepository, RegisterRepository


class IUnitOfWork(ABC):
    schedule: Type[ScheduleRepository]
    register: Type[RegisterRepository]

    @abstractmethod
    async def __init__(self):
        ...
    
    @abstractmethod
    async def __aenter__(self):
        ...
    
    @abstractmethod
    async def __aexit__(self, *args):
        ...
    
    @abstractmethod
    async def commit(self):
        ...
    
    @abstractmethod
    async def rollback(self):
        ...

class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker
    
    async def __aenter__(self):
        self.session = self.session_factory()

        self.schedule = ScheduleRepository(self.session)
        self.register = RegisterRepository(self.session)
    
    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()
    
    async def commit(self):
        await self.session.commit()
    
    async def rollback(self):
        await self.session.rollback()