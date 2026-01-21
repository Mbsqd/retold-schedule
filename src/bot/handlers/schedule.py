from datetime import datetime, timedelta

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.schedule.service import ScheduleService


def build_schedule_router(schedule_service: ScheduleService) -> Router:
    router = Router(name="schedule")

    @router.message(Command("current_week"))
    async def current_week(message: Message) -> None:
        today = datetime.today()
        text = schedule_service.get_format_schedule_by_week(today)
        await message.answer(text)

    @router.message(Command("next_week"))
    async def next_week(message: Message):
        today = datetime.today()
        next_week_date = today + timedelta(days=7)
        text = schedule_service.get_format_schedule_by_week(next_week_date)
        await message.answer(text)

    @router.message(Command("current_lesson"))
    async def current_lesson(message: Message):
        today = datetime.today()
        text = await schedule_service.get_format_lesson(today, True)
        await message.answer(text)

    @router.message(Command("next_lesson"))
    async def current_lesson(message: Message):
        today = datetime.today()
        text = await schedule_service.get_format_lesson(today, False)
        await message.answer(text)

    return router
