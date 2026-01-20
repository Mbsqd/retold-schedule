import json
from pathlib import Path
from typing import List

from src.consultations.models import ConsultationsModel
from src.consultations.schemas import ConsultationsShema


class ConsultationsLoader:
    def __init__(self, path: Path):
        self.path: Path = path

    def load(self) -> ConsultationsModel:
        with open(self.path, encoding="utf-8") as file:
            raw = json.loads(file.read())
            schema = ConsultationsShema.model_validate(raw)
            return ConsultationsModel(schema)
