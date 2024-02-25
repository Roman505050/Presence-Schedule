from src.database.models import Schedule, Groups
from src.utils.repository import SQLAlchemyRepository
from src.schemas.schedule import ScheduleSchema, GroupSchema, StudentsSchema

from sqlalchemy import select
from sqlalchemy.orm import selectinload

class ScheduleRepository(SQLAlchemyRepository):
    model = Schedule

    async def get_one_schedule(self, id: int) -> ScheduleSchema:
        stmt = (
            select(Schedule)
            .options(selectinload(Schedule.group).selectinload(Groups.students))
            .filter(Schedule.id == id)
        )
        res = await self.session.execute(stmt)
        res = res.scalars().first()
        if res is None:
            return None
        return ScheduleSchema(
            id=res.id,
            day=res.day,
            week=res.week,
            couple=res.couple,
            lesson=res.lesson,
            teacher=res.teacher,
            classroom=res.classroom,
            created_at=res.created_at,
            updated_at=res.updated_at,
            group=GroupSchema(
                students=[
                    StudentsSchema(
                        id=student.id,
                        last_name=student.last_name,
                        first_name=student.first_name,
                        patronymic_name=student.patronymic_name,
                        photo_id=student.photo_id,
                        telegram_id=student.telegram_id,
                        username=student.username,
                        role=student.role,
                        is_active=student.is_active,
                        created_at=student.created_at,
                        updated_at=student.updated_at
                    )for student in res.group.students]
                )
            )