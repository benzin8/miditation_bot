from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

start_router = Router()

@start_router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(f"Здравсвуйте! Укажите свое имя")