import asyncio
import logging
from zoneinfo import ZoneInfo

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import LinkPreviewOptions

from config import settings
from src.alert.dependencies import get_alert_service
from src.bot.routers import setup_routers
from src.consultations.dependencies import get_consultations_service
from src.notification.notification_manager import NotificationManager
from src.notification.scheduler import NotificationScheduler
from src.notification.sender import TelegramNotificationSender
from src.notification.service import NotificationService
from src.schedule.dependencies import get_schedule_service


def create_notification_service(bot: Bot) -> NotificationService:
    sender = TelegramNotificationSender(bot, settings.telegram_admin_id)
    scheduler = NotificationScheduler(sender=sender, tz=ZoneInfo(settings.timezone))

    return NotificationService(scheduler=scheduler, tz=ZoneInfo(settings.timezone))


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bot_token,
              default=DefaultBotProperties(
                  parse_mode=ParseMode.HTML,
                  link_preview=LinkPreviewOptions(is_disabled=True)))

    dp = Dispatcher()

    alert_service = get_alert_service()

    schedule_service = get_schedule_service(alert_service)
    consultations_service = get_consultations_service()

    notification_service = create_notification_service(bot)
    manager = NotificationManager(
        schedule_service=schedule_service,
        notification_service=notification_service,
        tz=ZoneInfo(settings.timezone)
    )
    asyncio.create_task(manager.run())

    setup_routers(dp, schedule_service, consultations_service)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Shutting down...")
