from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from core.database import async_session

from backend.services import add_name, add_email

register_router = Router()

class RegistrationStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_email = State()


@register_router.message(Command("registration"))
async def registration(message: Message, state: FSMContext):
    result_name = await add_name(
        telegram_id= message.from_user.id,
    )
    # result_email = await add_email(
    #     telegram_id= message.from_user.id
    # )
    if result_name == False:
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
      )
   
        print(f"Имя для пользователя {message.from_user.id} добавленно - {name}")
        if user:
            await message.answer(
                f"✅ Отлично, {name}!\n"
                f"Пожалуйста, введите ваш email:\n"
            )
            await state.clear()
        await state.set_state(RegistrationStates.waiting_for_email)


    except Exception as e:
        print(f"Ошибка при добавлении имени для пользователя {message.from_user.id}: {e}")
        await message.answer("Произошла ошибка")


@register_router.message(RegistrationStates.waiting_for_email)
async def email_process(message: Message, state: FSMContext):
    email = message.text.strip()

    if "@" not in email or "." not in email:
        await message.answer("❌ Пожалуйста, введите корректный email:")
        return
    
    if len(email) > 100:
        await message.answer("❌ Слишком длинный email. Введите покороче:")
        return
    
    try:
        await add_email(
            telegram_id=message.from_user.id,
            email=email,
            is_registrated=True
        )
    except Exception as e:
        print(f"Ошибка при добавлении email для пользователя {message.from_user.id}: {e}")
        await message.answer("Произошла ошибка при сохранении email. Попробуйте еще раз.")
        return
        
    await message.answer(f"✅ Спасибо! Ваш email {email} сохранен.\n"
                         f"Регистрация завершена.")
    await state.clear()