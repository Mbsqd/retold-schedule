import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import LinkPreviewOptions

from config import settings
from src.utils.schedule_utils import ScheduleProcessor
from src.utils.consultation_utils import ConsultationsProcessor

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bot_token,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML, link_preview=LinkPreviewOptions(is_disabled=True)))
dp = Dispatcher()

schedule_processor = ScheduleProcessor()
consultation_processor = ConsultationsProcessor()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = schedule_processor.generate_schedule_message_for_week(True)
    await message.answer(text)


@dp.message(Command("current_week"))
async def cmd_current_week(message: types.Message):
    text = schedule_processor.generate_schedule_message_for_week(True)
    await message.answer(text)


@dp.message(Command("next_week"))
async def cmd_next_week(message: types.Message):
    text = schedule_processor.generate_schedule_message_for_week(False)
    await message.answer(text)


@dp.message(Command("current_lesson"))
async def cmd_lesson(message: types.Message):
    text = schedule_processor.generate_lesson_message(True)
    await message.answer(text)


@dp.message(Command("next_lesson"))
async def cmd_next_lesson(message: types.Message):
    text = schedule_processor.generate_lesson_message(False)
    await message.answer(text)


@dp.message(Command("consultations"))
async def cmd_consultations(message: types.Message):
    text = consultation_processor.generate_consultations_message()
    await message.answer(text)


async def main():
    print()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
