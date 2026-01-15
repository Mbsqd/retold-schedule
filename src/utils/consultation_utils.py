from src.config import settings
from src.model.consultations import ConsultationsModel, ConsultationModel
from src.utils import json_utils

from aiogram import html


def process_consultations_json() -> ConsultationsModel:
    raw_consultations = json_utils.open_json(settings.path_to_consultations_file)
    consultations: ConsultationsModel = json_utils.validate_consultation(raw_consultations)
    return consultations


class ConsultationsProcessor:
    def __init__(self):
        self.consultations: ConsultationsModel = process_consultations_json()

    def generate_consultations_message(self) -> str:
        message_text: str = ""

        consultations: list[ConsultationModel] = self.consultations.consultations
        for consultation in consultations:
            message_text += f"{html.bold(consultation.day.value)}\n"
            for item in consultation.items:
                message_text += (f"{html.italic(item.start_time.strftime('%H:%M'))} - "
                                 f"{html.link(item.subject, item.zoom)}, "
                                 f"{html.bold(item.teacher)}\n")

            message_text += "\n"

        return message_text
