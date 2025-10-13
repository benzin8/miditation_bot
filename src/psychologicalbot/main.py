import logging
from aiogram import Bot, Dispatcher
from core import load_config
from psychologicalbot.handlers import start_router, register_router

config = load_config()
bot = Bot(token=config.bot_token)

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(register_router)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())