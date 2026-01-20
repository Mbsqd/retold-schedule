from functools import lru_cache

from src.config import settings
from src.schedule.loader import ScheduleLoader
from src.schedule.service import ScheduleService

@lru_cache
def get_schedule_service() -> ScheduleService:
    loader = ScheduleLoader(settings.path_to_schedule_file)
    schedule = loader.load()
    return ScheduleService(schedule)
