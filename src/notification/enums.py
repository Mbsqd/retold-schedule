from enum import Enum


class NotificationStatusEnum(str, Enum):
    pending = "pending"
    success = "success"
    cancelled = "cancelled"
