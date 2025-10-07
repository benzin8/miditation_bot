import logging
from aiogram import Bot, Dispatcher
from core import load_config

config = load_config()
print(config.bot_token)
bot = Bot(token=config.bot_token)

dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())