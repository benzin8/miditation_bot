from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from psychologicalbot.keyboards.tasks import TaskKeyboards
from backend.services.task_service import get_random_task, execute_task


router = Router()


class TaskStates(StatesGroup):
    active_task = State()

@router.message(F.text == "Получить задачу")
async def get_random_task_handler(message: Message, state: FSMContext) -> None:
    try:
        task = await get_random_task()
        if task:
            await state.update_data(task_id = task.task_id)
            await state.set_state(TaskStates.active_task)
            message_text = (
                f"Задача: {task.title}\n"
                f"Описание: {task.description}\n"
                f"Категория: {task.category}\n"
                f"Статус выполнения: {"Выполено" if task.complited == True else "Не выполнено"}"
            )
            await message.answer(message_text, reply_markup=await TaskKeyboards.manage_task_keyboard())
        else:
            await message.answer("Нет доступных задач.")
    except Exception as e:
        await message.answer("Произошла ошибка при получении задачи.")
        print(f"Error fetching task: {e}")

@router.message(F.text == "Выполнить")
async def execute_task_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state != TaskStates.active_task:
        await message.answer("Сначала получите задачу")
        return
    
    data = await state.get_data()
    print(data)
    task_id = data.get('task_id')

    if task_id:
        await execute_task(task_id)
        await message.answer("Задача выполнена", reply_markup=await TaskKeyboards.get_task_keyboard())
        await state.clear()
    else:
        await message.answer("Задача не найдена")