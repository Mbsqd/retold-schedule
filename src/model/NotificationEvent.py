from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from src.model import LessonModel


class NotificationStatusEnum(str, Enum):
    pending = "pending"
    success = "success"


class NotificationEvent(BaseModel):
    notify_at: datetime
    lesson_start: datetime
    subject: str
    status: NotificationStatusEnum