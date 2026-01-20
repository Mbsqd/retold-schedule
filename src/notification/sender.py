from abc import ABC, abstractmethod

from aiogram import Bot


class NotificationSender(ABC):
    @abstractmethod
    async def send(self, text: str) -> None:
        ...


class TelegramNotificationSender(NotificationSender):
    def __init__(self, bot: Bot, chat_id: int):
        self.bot = bot
        self.chat_id = chat_id

    async def send(self, text: str) -> None:
        await self.bot.send_message(chat_id=self.chat_id, text=text)
