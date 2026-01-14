from datetime import time
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class TypeOfWeekEnum(str, Enum):
    numerator = "numerator"
    denominator = "denominator"


class DayOfWeekEnum(str, Enum):
    monday = "Понеділок"
    tuesday = "Вівторок"
    wednesday = "Середа"
    thursday = "Четвер"
    friday = "П'ятниця"
    saturday = "Субота"
    sunday = "Неділя"


class TypeLessonEnum(str, Enum):
    lecture = "lecture"
    practice = "practice"


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
