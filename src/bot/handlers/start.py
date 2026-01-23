from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import html

from src.bot.keyboards.main_keyboard import main_keyboard

router = Router()

START_MESSAGE = (
    f"{html.bold("Вітаю! 👋")}\n\n"
    "Я - бот, який допоможе Вам з розкладом занять і консультацій.\n"
    "Допоможу швидко дізнатись:\n\n"
    "- яке зараз заняття\n"
    "- що буде далі\n"
    "- розклад на тиждень\n"
    "- чи є повітряна тривога"
)


@router.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer(START_MESSAGE, reply_markup=main_keyboard())
