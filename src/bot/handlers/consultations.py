from aiogram import Router, F
from aiogram.types import Message

from src.bot.keyboards.enums import MainMenu
from src.consultations.service import ConsultationsService


def build_consultation_router(consult_service: ConsultationsService) -> Router:
    router = Router(name="consultations")

    @router.message(F.text == MainMenu.CONSULTATIONS)
    async def get_consultations(message: Message):
        text = consult_service.get_format_consultations()
        await message.answer(text)

    return router
