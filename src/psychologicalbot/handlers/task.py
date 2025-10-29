from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from psychologicalbot.keyboards.tasks import TaskKeyboards
from backend.services.task_service import get_random_task

router = Router()

@router.message(F.text == "Получить задачу")
async def get_random_task_handler(message: Message) -> None:
    try:
        task = await get_random_task()
        if task:
            message_text = (
                f"Задача: {task.title}\n"
                f"Описание: {task.description}\n"
                f"Категория: {task.category}\n"
                f"Статус выполнения: {"Выполено" if task.complited == True else "Не выполнено"}"
            )
            await message.answer(message_text, reply_markup=await TaskKeyboards.get_task_keyboard())
        else:
            await message.answer("Нет доступных задач.")
    except Exception as e:
        await message.answer("Произошла ошибка при получении задачи.")
        print(f"Error fetching task: {e}")