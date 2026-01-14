from datetime import time
from typing import List

from pydantic import BaseModel

from src.model.enums import DayOfWeekEnum


class ItemModel(BaseModel):
    start_time: time
    end_time: time
    subject: str
    teacher: str
    zoom: str


class ConsultationModel(BaseModel):
    day: str
    label: DayOfWeekEnum
    items: List[ItemModel]


class ConsultationsModel(BaseModel):
    consultations: List[ConsultationModel]
