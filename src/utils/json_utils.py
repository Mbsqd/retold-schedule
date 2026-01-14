import json
from pathlib import Path

from config import settings
from src.model.schedule import ScheduleModel

def open_json():
    with open(settings.path_to_file, "r", encoding="utf-8") as file:
        raw_schedule = json.loads(file.read())
        return raw_schedule


def validate_schedule(raw_schedule) -> ScheduleModel:
    schedule = ScheduleModel.model_validate(raw_schedule)
    return schedule


