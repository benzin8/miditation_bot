from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from backend.services import create_user

start_router = Router()

@start_router.message(Command("start"))
async def start_command(message: Message):
    telegram_id = message.from_user.id
    await create_user(
        telegram_id=telegram_id
    )
    await message.answer(f"Здравствуйте! Завершите регистрацию командой /registration")