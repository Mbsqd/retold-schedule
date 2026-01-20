from datetime import time
from typing import List

from src.schedule.enums import TypeOfWeekEnum, DayOfWeekEnum, TypeLessonEnum
from src.schedule.schemas import LessonSchema, DaySchema, WeekSchema, ScheduleSchema


class LessonModel:
    def __init__(self, lesson_schema: LessonSchema):
        self.start_time: time = lesson_schema.start_time
        self.end_time: time = lesson_schema.end_time
        self.subject: str = lesson_schema.subject
        self.type_lesson: TypeLessonEnum = lesson_schema.type_lesson
        self.is_online: bool = lesson_schema.is_online
        self.auditory: str = lesson_schema.auditory or ""
        self.zoom: str = lesson_schema.zoom
        self.zoom_2: str = lesson_schema.zoom_2 or ""


class DayModel:
    def __init__(self, day_schema: DaySchema):
        self.day: DayOfWeekEnum = day_schema.day
        self.label: str = day_schema.label
        self.lessons: List[LessonModel] = [
            LessonModel(lesson) for lesson in day_schema.lessons
        ]


class WeekModel:
    def __init__(self, week_schema: WeekSchema):
        self.type_of_week: TypeOfWeekEnum = week_schema.type_of_week
        self.label: str = week_schema.label
        self.days: List[DayModel] = [
            DayModel(day) for day in week_schema.days
        ]

    def get_day(self, day_of_week: DayOfWeekEnum) -> DayModel | None:
        for day in self.days:
            if day.day == day_of_week:
                return day
        return None


class ScheduleModel:
    def __init__(self, schedule_schema: ScheduleSchema):
        self.weeks: List[WeekModel] = [
            WeekModel(week_schema) for week_schema in schedule_schema.weeks
        ]

    def get_week(self, week_type) -> WeekModel | None:
        for week in self.weeks:
            if week.type_of_week == week_type:
                return week
        return None
