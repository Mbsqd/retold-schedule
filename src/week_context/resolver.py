from datetime import datetime
from zoneinfo import ZoneInfo

from src.week_context.models import WeekContext


class WeekContextResolver:
    def __init__(self, tz: ZoneInfo):
        self.tz = tz

    def resolve(self) -> WeekContext:
        today = datetime.now(self.tz).date()
        return WeekContext.from_date(today)
