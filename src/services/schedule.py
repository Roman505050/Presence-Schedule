from src.utils.unitofwork import IUnitOfWork
from src.schemas.schedule import ScheduleSchema

class ScheduleService:
    async def get_students_schedule(self, uow: IUnitOfWork, schedule_id: int) -> ScheduleSchema | None:
        async with uow:
            data = await uow.schedule.get_one_schedule(schedule_id)
            return data