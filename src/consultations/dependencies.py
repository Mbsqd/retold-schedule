from functools import lru_cache

from src.config import settings
from src.consultations.loader import ConsultationsLoader
from src.consultations.service import ConsultationsService


@lru_cache
def get_consultations_service():
    loader = ConsultationsLoader(settings.path_to_consultations_file)
    consultations = loader.load()
    return ConsultationsService(consultations)