from datetime import time
from typing import List

from src.consultations.schemas import ItemSchema, ConsultationSchema, ConsultationsShema
from src.schedule.enums import DayOfWeekEnum


class ItemModel:
    def __init__(self, item_schema: ItemSchema):
        self.start_time: time = item_schema.start_time
        self.end_time: time = item_schema.end_time
        self.subject: str = item_schema.subject
        self.teacher: str = item_schema.teacher
        self.zoom: str = item_schema.zoom


class ConsultationModel:
    def __init__(self, consultation_schema: ConsultationSchema):
        self.day: DayOfWeekEnum = consultation_schema.day
        self.label: str = consultation_schema.label
        self.items: List[ItemModel] = [
            ItemModel(item) for item in consultation_schema.items
        ]


class ConsultationsModel:
    def __init__(self, consultations_schema: ConsultationsShema):
        self.consultations: List[ConsultationModel] = [
            ConsultationModel(consultation) for consultation in consultations_schema.consultations
        ]
