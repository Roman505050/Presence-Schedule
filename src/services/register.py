from src.utils.unitofwork import IUnitOfWork
from src.schemas import RegisterCreateSchema, RegisterSchema


class RegisterService:
    async def add_register(self, uow: IUnitOfWork, register: RegisterCreateSchema) -> None:
        async with uow:
            register = await uow.register.add_one(register.model_dump())
            await uow.commit()
            return RegisterSchema(
                id=register.id,
                student_id=register.student_id,
                schedule_id=register.schedule_id,
                date=register.date,
                created_at=register.created_at,
                updated_at=register.updated_at,
                presence=register.presence
            )