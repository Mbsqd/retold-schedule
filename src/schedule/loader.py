import json
from pathlib import Path

from src.schedule.models import ScheduleModel
from src.schedule.schemas import ScheduleSchema


class ScheduleLoader:
    def __init__(self, path: Path):
        self.path: Path = path

    def load(self) -> ScheduleModel:
        with open(self.path, encoding="utf-8") as file:
            raw = json.loads(file.read())
            schema = ScheduleSchema.model_validate(raw)
            return ScheduleModel(schema)