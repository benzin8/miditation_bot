from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


class RegistrationKeyboards:
    @staticmethod
    def get_registration_keyboard() -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Регистрация")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )