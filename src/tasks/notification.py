import aiohttp
import pytz
import datetime

from src.config import settings
from src.services import ScheduleService, RegisterService
from src.schemas import RegisterCreateSchema
from src.utils.unitofwork import IUnitOfWork, UnitOfWork


async def send_message(schedule_id: int):
    uow: IUnitOfWork = UnitOfWork()
    data = await ScheduleService().get_students_schedule(uow, schedule_id)
    if data is None:
        return
    URL = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage"
    UTC_NOW = datetime.datetime.utcnow()
    KIEV_NOW = UTC_NOW.astimezone(pytz.timezone(settings.TIMEZONE))
    for student in data.group.students:
        register = await RegisterService().add_register(
            uow, 
            register=RegisterCreateSchema(
                student_id=student.id,
                schedule_id=schedule_id,
                date=KIEV_NOW.date(),
            )
        )
        keyboard = {
            'inline_keyboard': [
                [
                    {
                        'text': '✅ Присутній',
                        'callback_data': f'present:{register.id}'
                    },
                    {
                        'text': '❌ Відсутній',
                        'callback_data': f'absent:{register.id}'
                    }
                ]
            ]
        }
        data = {
            'chat_id': student.telegram_id,
            'text': f'Пара: {data.couple}\nПредмет: {data.lesson}\nВикладач: {data.teacher}\nАудиторія: {data.classroom}',
            'reply_markup': keyboard
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(URL, json=data) as response:
                await response.json()
