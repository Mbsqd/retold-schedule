from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from src.bot.keyboards.enums import MainMenu


def main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=MainMenu.CURRENT_WEEK),
                KeyboardButton(text=MainMenu.NEXT_WEEK),
            ],
            [
                KeyboardButton(text=MainMenu.CONSULTATIONS),
            ],
            [
                KeyboardButton(text=MainMenu.CURRENT_LESSON),
                KeyboardButton(text=MainMenu.NEXT_LESSON),
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder="Оберіть дію"
    )
