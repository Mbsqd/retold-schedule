from datetime import time
from typing import Optional

from pydantic import BaseModel, Field

from src.model.enums import TypeLessonEnum, DayOfWeekEnum, TypeOfWeekEnum


class LessonModel(BaseModel):
    start_time: time
    end_time: time
    subject: str
    type_lesson: TypeLessonEnum = Field(alias="type")
    is_online: bool
    auditory: Optional[str] = ""
    zoom: str
    zoom_2: Optional[str] = ""
    model_config = {"extra": "forbid"}


class DayModel(BaseModel):
    day: str
    label: DayOfWeekEnum
    lessons: list[LessonModel]


class WeekModel(BaseModel):
    typeOfWeek: TypeOfWeekEnum = Field(alias="type")
    label: str
    days: list[DayModel]


class ScheduleModel(BaseModel):
    weeks: list[WeekModel]
