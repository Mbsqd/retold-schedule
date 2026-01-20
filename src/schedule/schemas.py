from datetime import time
from typing import Optional, List

from pydantic import BaseModel, Field

from src.schedule.enums import TypeLessonEnum, DayOfWeekEnum, TypeOfWeekEnum


class LessonSchema(BaseModel):
    start_time: time
    end_time: time
    subject: str
    type_lesson: TypeLessonEnum = Field(alias="type")
    is_online: bool
    auditory: Optional[str] = ""
    zoom: str
    zoom_2: Optional[str] = ""
    model_config = {"extra": "forbid"}


class DaySchema(BaseModel):
    day: DayOfWeekEnum
    label: str
    lessons: List[LessonSchema]


class WeekSchema(BaseModel):
    type_of_week: TypeOfWeekEnum = Field(alias="type")
    label: str
    days: List[DaySchema]


class ScheduleSchema(BaseModel):
    weeks: List[WeekSchema]
