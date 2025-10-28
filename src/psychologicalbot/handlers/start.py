from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from backend.services import create_user, get_user

start_router = Router()

@start_router.message(Command("start"))
async def start_command(message: Message):
    telegram_id = message.from_user.id
    await create_user(
        telegram_id=telegram_id
    )
    user = await get_user(telegram_id=telegram_id)
    if user.is_registrated == True:
        await message.answer("Здравствуйте! Рады видеть вас снова.")
    else:
        await message.answer(f"Здравствуйте! Завершите регистрацию командой /registration")