import asyncio
import logging
from datetime import datetime
from zoneinfo import ZoneInfo

from aiogram import Bot, Dispatcher, types, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import LinkPreviewOptions

from config import settings
from src.model.NotificationEvent import NotificationStatusEnum, NotificationEvent
from src.utils.NotificationPlanner import add_lesson_notification
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
    chat_id = message.chat.id
    print(chat_id)
    await message.answer(text)


async def run_notification(event: NotificationEvent) -> None:
    now = datetime.now(ZoneInfo("Europe/Kyiv"))

    delay = (event.notify_at - now).total_seconds()

    print(
        f"⏰ Notification scheduled: {event.subject} "
        f"at {event.notify_at.isoformat()}"
    )

    if delay > 0:
        await asyncio.sleep(delay)

    # Send message
    await send_notify(event)

    event.status = NotificationStatusEnum.success


async def send_notify(event: NotificationEvent):
    text = f"{html.bold("Заняття через 5 хв")}\n\n"
    text += f"{event.subject}\n"
    text += f"{event.lesson_start.strftime('%H:%M')}\n"
    # Добавить ссылки

    # await bot.send_message(..., text)


async def main():
    events = add_lesson_notification()

    for event in events:
        if event.status != NotificationStatusEnum.pending:
            continue

        asyncio.create_task(run_notification(event))

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
