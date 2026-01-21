from functools import lru_cache

from src.alert.service import AlertService
from src.config import settings
from src.schedule.loader import ScheduleLoader
from src.schedule.service import ScheduleService

@lru_cache
def get_schedule_service(alert_service: AlertService) -> ScheduleService:
    loader = ScheduleLoader(settings.path_to_schedule_file)
    schedule = loader.load()
    return ScheduleService(schedule, alert_service)
