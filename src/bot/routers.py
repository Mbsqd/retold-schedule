from aiogram import Bot, Dispatcher

from src.bot.handlers.consultations import build_consultation_router
from src.bot.handlers.schedule import build_schedule_router
from src.consultations.service import ConsultationsService
from src.schedule.service import ScheduleService


def setup_routers(dp: Dispatcher,
                  schedule_service: ScheduleService,
                  consultations_service: ConsultationsService
                  ) -> None:
    dp.include_routers(
        build_schedule_router(schedule_service),
        build_consultation_router(consultations_service)
    )
