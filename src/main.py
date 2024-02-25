import schedule
import aiohttp
import asyncio
import pytz

from src.tasks.notification import send_message


def send_message_task(schedule_id: int):
    asyncio.create_task(send_message(schedule_id=schedule_id))

def tasks():
    tz = pytz.timezone('Europe/Kiev')
    schedule.every().day.at("15:15").do(send_message_task, 1).tag('send_message').timezone = tz
    schedule.every().day.at("15:16").do(send_message_task, 1).tag('send_message').timezone = tz

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