import aiohttp

from src.config import settings
from src.services.schedule import ScheduleService
from src.utils.unitofwork import IUnitOfWork, UnitOfWork


async def send_message(schedule_id: int):
    uow: IUnitOfWork = UnitOfWork()
    data = await ScheduleService().get_students_schedule(uow, schedule_id)
    if data is None:
        return
    URL = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage"
    for student in data.group.students:
        keyboard = {
            'inline_keyboard': [
                [
                    {
                        'text': '✅ Присутній',
                        'callback_data': 'present'
                    },
                    {
                        'text': '❌ Відсутній',
                        'callback_data': 'absent'
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
