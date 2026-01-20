from datetime import datetime

from src.notification.enums import NotificationStatusEnum


class Notification:
    def __init__(self, notify_at: datetime, text: str):
        self.notify_at: datetime = notify_at
        self.text: str = text
        self.status: NotificationStatusEnum = NotificationStatusEnum.pending
