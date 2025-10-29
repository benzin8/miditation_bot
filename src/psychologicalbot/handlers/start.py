from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from backend.services import create_user, get_user
from psychologicalbot.keyboards import TaskKeyboards, RegistrationKeyboards

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
        await message.answer("Выберите действие:", reply_markup=await TaskKeyboards.get_task_keyboard())
    else:
        await message.answer(f"Здравствуйте! Завершите регистрацию командой /registration")
        await message.answer("Нажмите на кнопку", reply_markup=RegistrationKeyboards.get_registration_keyboard())