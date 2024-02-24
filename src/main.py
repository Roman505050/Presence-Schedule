import schedule
import aiohttp
import asyncio
import pytz

from src.tasks.notification import send_message


def send_message_task(text):
    asyncio.create_task(send_message(text=text))

def tasks():
    tz = pytz.timezone('Europe/Kiev')
    schedule.every().saturday.at("21:26").do(send_message_task, schedule_id=1).timezone = tz

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