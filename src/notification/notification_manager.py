import asyncio
import logging
from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo

from src.notification.service import NotificationService
from src.schedule.service import ScheduleService


class NotificationManager:
    def __init__(self, schedule_service: ScheduleService, notification_service: NotificationService, tz: ZoneInfo):
        self.schedule_service = schedule_service
        self.notification_service = notification_service
        self.tz = tz

    async def run(self):
        while True:
            today = date.today()
            events = self.schedule_service.build_week_events(today)
            notifications = self.notification_service.build_notifications(events)

            await self.notification_service.schedule_all(notifications)
            await self._sleep_until_next_week()

    async def _sleep_until_next_week(self) -> None:
        now = datetime.now(tz=self.tz)

        days_until_monday = (7 - now.weekday()) % 7
        if days_until_monday == 0:
            days_until_monday = 7

        next_monday = (now + timedelta(days=days_until_monday)).replace(hour=0, minute=0, second=0, microsecond=0)

        delay = (next_monday - now).total_seconds()

        await asyncio.sleep(delay)
