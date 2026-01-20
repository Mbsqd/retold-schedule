import logging

from aiogram import Router, Bot, Dispatcher

router = Router()


async def on_shutdown( bot: Bot):
    logging.warning("Bot is shutting down...")
    await bot.session.close()
