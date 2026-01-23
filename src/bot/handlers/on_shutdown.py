import logging

from aiogram import Router, Bot, Dispatcher

from src.alert.service import AlertService

router = Router()


async def on_shutdown(bot: Bot, dispatcher: Dispatcher):
    logging.warning("Bot is shutting down...")

    alert_service: AlertService = dispatcher["alert_service"]
    await alert_service.client.stop()

    await bot.session.close()
