from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

class TaskKeyboards:
    @staticmethod
    async def get_task_keyboard() -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Получить задачу")],
                [KeyboardButton(text="Мои задачи"), KeyboardButton(text="Главное меню")],
            ],
            resize_keyboard=True
        )
    