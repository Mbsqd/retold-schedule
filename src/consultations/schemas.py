from datetime import time
from typing import List

from pydantic import BaseModel

from src.schedule.enums import DayOfWeekEnum


class ItemSchema(BaseModel):
    start_time: time
    end_time: time
    subject: str
    teacher: str
    zoom: str


class ConsultationSchema(BaseModel):
    day: DayOfWeekEnum
    label: str
    items: List[ItemSchema]


class ConsultationsShema(BaseModel):
    consultations: List[ConsultationSchema]
