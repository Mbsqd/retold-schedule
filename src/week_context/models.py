from datetime import date, timedelta, datetime

from src.schedule.enums import TypeOfWeekEnum, DayOfWeekEnum

NUMERATOR_START_WEEK = date(2025, 1, 1)

class WeekContext:
    def __init__(self, week_start_date: date, week_end_date: date, type_of_week: TypeOfWeekEnum):
        self.week_start_date = week_start_date
        self.week_end_date = week_end_date
        self.type_of_week = type_of_week


    @classmethod
    def from_date(cls, target_date: date | datetime) -> WeekContext:
        if isinstance(target_date, datetime):
            target_date = target_date.date()

        weekday = target_date.weekday()
        start = target_date - timedelta(days=weekday)
        end = target_date + timedelta(days=6)

        delta_weeks = (start - NUMERATOR_START_WEEK).days // 7

        type_of_week = (
            TypeOfWeekEnum.numerator
            if delta_weeks % 2 == 0
            else TypeOfWeekEnum.denominator
        )

        return cls(start, end, type_of_week)