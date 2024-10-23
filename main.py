import asyncio
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from bot.handlers.start_handlers import router
from bot.config import TOKEN


async def main():
    bot = Bot(token=TOKEN)
    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('End work')

