from src.consultations.models import ConsultationsModel, ConsultationModel

from aiogram import html


class ConsultationsService:
    def __init__(self, consultations: ConsultationsModel):
        self.consultations = consultations

    def get_format_consultations(self) -> str:
        consultations: list[ConsultationModel] = self.consultations.consultations
        text: str = ""

        for consultation in consultations:
            text += f"{html.bold(consultation.label)}\n"
            for item in consultation.items:
                text += (f"{html.italic(item.start_time.strftime('%H:%M'))} - "
                         f"{html.link(item.subject, item.zoom)}, "
                         f"{html.bold(item.teacher)}\n")

            text += "\n"

        if not text:
            return "На поточний момент консультацій немає"
        return text
