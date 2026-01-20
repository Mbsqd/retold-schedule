from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.consultations.service import ConsultationsService


def build_consultation_router(consult_service: ConsultationsService) -> Router:
    router = Router(name="consultations")

    @router.message(Command("consultations"))
    async def get_consultations(message: Message):
        text = consult_service.get_format_consultations()
        await message.answer(text)

    return router
