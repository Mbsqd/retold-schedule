from aiogram import Bot, Dispatcher

from src.alert.service import AlertService
from src.bot.handlers import start
from src.bot.handlers.consultations import build_consultation_router
from src.bot.handlers.on_shutdown import on_shutdown
from src.bot.handlers.schedule import build_schedule_router
from src.consultations.service import ConsultationsService
from src.schedule.service import ScheduleService


def setup_routers(dp: Dispatcher,
                  schedule_service: ScheduleService,
                  consultations_service: ConsultationsService
                  ) -> None:
    dp.include_routers(
        start.router,
        build_schedule_router(schedule_service),
        build_consultation_router(consultations_service)
    )

    dp.shutdown.register(on_shutdown)
