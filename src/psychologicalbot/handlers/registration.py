from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from core.database import async_session

from backend.services import add_name

register_router = Router()

class RegistrationStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_email = State()


@register_router.message(Command("registration"))
async def registration(message: Message, state: FSMContext):
    result = await add_name(
        telegram_id= message.from_user.id,
        # name=message.from_user.first_name or "Неизвестный"
    )
    if result == False:
        await message.answer("Вы уже зарегистрированы.")
        return
    else:
        await message.answer("Как вас зовут?")
        await state.set_state(RegistrationStates.waiting_for_name)

@register_router.message(RegistrationStates.waiting_for_name)
async def name_process(message: Message, state: FSMContext):
    name = message.text.strip()

    if len(name) < 2:
        await message.answer("❌ Имя слишком короткое. Введите настоящее имя:")
        return
    
    if len(name) > 50:
        await message.answer("❌ Имя слишком длинное. Введите имя покороче:")
        return
    
    try:
        user = await add_name(
            telegram_id= message.from_user.id,
            name=name,
            is_registrated=True
      )
   
        print(f"Имя для пользователя {message.from_user.id} добавленно - {name}")
        if user:
            await message.answer(
                f"✅ Отлично, {name}!\n"
                f"Регистрация завершена.\n"
                f"Ваш ID: {user.telegram_id}"
            )
            await state.clear()

    except Exception as e:
        print(f"Ошибка при добавлении имени для пользователя {message.from_user.id}: {e}")
        await message.answer("Произошла ошибка")


