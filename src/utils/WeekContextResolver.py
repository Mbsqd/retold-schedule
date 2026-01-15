from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from src.model import TypeOfWeekEnum
from src.model.WeekContext import WeekContext


# Добавить проверку на спец. неделю
def week_context_resolver() -> WeekContext:
    tz_ua = ZoneInfo("Europe/Kyiv")
    current_datetime = datetime.now(tz_ua)
    current_date = current_datetime.date()
    current_weekday = current_datetime.date().weekday()
    days_until_sunday = 6 - current_weekday
    current_week_number = current_date.isocalendar().week

    start_week_date = current_date - timedelta(days=current_weekday)
    end_week_date = current_date + timedelta(days=days_until_sunday)

    if current_week_number % 2 == 0:
        type_of_week = TypeOfWeekEnum.numerator
    else:
        type_of_week = TypeOfWeekEnum.denominator

    return WeekContext(week_start_date=start_week_date, week_end_date=end_week_date, type_of_week=type_of_week)
