import schedule
import asyncio
import pytz

from src.tasks.notification import send_message
from src.config import settings


def send_message_task(schedule_id: int):
    asyncio.create_task(send_message(schedule_id=schedule_id))

def tasks():
    tz = pytz.timezone(settings.TIMEZONE)
    schedule.every().monday.at("08:00").do(send_message_task, 1).tag('send_message').timezone = tz
    schedule.every().monday.at("09:30").do(send_message_task, 2).tag('send_message').timezone = tz
    schedule.every().monday.at("11:00").do(send_message_task, 3).tag('send_message').timezone = tz
    schedule.every().monday.at("14:10").do(send_message_task, 4).tag('send_message').timezone = tz
    schedule.every(10).seconds.do(send_message_task, 2).timezone = tz
    schedule.every(10).seconds.do(send_message_task, 2).timezone = tz

async def main():
    tasks()
    try:
        while True:
            schedule.run_pending()
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print('Program was stopped!')

if __name__ == "__main__":
    asyncio.run(main())