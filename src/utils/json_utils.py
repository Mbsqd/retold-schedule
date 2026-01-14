import json
from pathlib import Path

from config import settings
from src.model.consultations import ConsultationsModel
from src.model.schedule import ScheduleModel

def open_json(path_to_file: Path):
    with open(path_to_file, "r", encoding="utf-8") as file:
        raw_json = json.loads(file.read())
        return raw_json


def validate_schedule(raw_schedule) -> ScheduleModel:
    schedule = ScheduleModel.model_validate(raw_schedule)
    return schedule

def validate_consultation(raw_consultation) -> ConsultationsModel:
    consultation = ConsultationsModel.model_validate(raw_consultation)
    return consultation
