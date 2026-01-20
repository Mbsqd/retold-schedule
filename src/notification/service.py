import asyncio
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from aiogram import html

from src.notification.model import Notification
from src.notification.scheduler import NotificationScheduler
from src.schedule.lesson_event import LessonEvent
from src.utils.formatter_lesson_links import get_formatted_lesson_links


class NotificationService:
    def __init__(self, scheduler: NotificationScheduler, tz: ZoneInfo):
        self.scheduler = scheduler
        self.tz = tz

    def build_notifications(self, events: list[LessonEvent], minutes_before: int = 5) -> list[Notification]:
        now = datetime.now(tz=self.tz)
        notifications: list[Notification] = []

        for event in events:
            notify_at = event.start_at - timedelta(minutes=minutes_before)

            if notify_at <= now:
                continue

            notifications.append(Notification(
                notify_at=notify_at,
                text=f"{html.bold("Заняття через 5хв")} - {html.italic(event.start_at.strftime('%H:%M'))}\n\n"
                     f"{event.title} - {get_formatted_lesson_links(event)}"
            ))
            print(f"Created notifications: {notify_at} - {event.title}")

        return notifications

    async def schedule_all(self, notifications: list[Notification]) -> None:
        await asyncio.gather(
            *[self.scheduler.schedule(n) for n in notifications]
        )
