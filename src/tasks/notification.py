import aiohttp

from src.config import settings



async def send_message(schedule_id: int):
    URL = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": 734116381,
        "text": 'text'
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(URL, data=data) as response:
            return await response.text()
