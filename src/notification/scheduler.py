import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo

from src.notification.enums import NotificationStatusEnum
from src.notification.model import Notification
from src.notification.sender import NotificationSender


class NotificationScheduler:
    def __init__(self, sender: NotificationSender, tz: ZoneInfo):
        self.sender = sender
        self.tz = tz

    async def schedule(self, notification: Notification) -> None:
        now = datetime.now(tz=self.tz)
        delay = (notification.notify_at - now).total_seconds()

        if delay > 0:
            await asyncio.sleep(delay)


        await self.sender.send(notification.text)
        notification.status = NotificationStatusEnum.success