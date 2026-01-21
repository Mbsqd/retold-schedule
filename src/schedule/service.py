from datetime import date, timedelta, datetime, time, timezone
from typing import List
from zoneinfo import ZoneInfo

from aiogram import html

from src.alert.service import AlertService
from src.config import settings
from src.schedule.enums import DayOfWeekEnum, DAY_OFFSET
from src.schedule.lesson_event import LessonEvent
from src.schedule.models import ScheduleModel, WeekModel, LessonModel, DayModel
from src.utils.formatter_lesson_links import get_formatted_lesson_links
from src.week_context.models import WeekContext


class ScheduleService:
    def __init__(self, schedule: ScheduleModel, alert_service: AlertService):
        self.schedule = schedule
        self.alert_service = alert_service

    def get_week_by_date(self, target_date: date) -> WeekModel:
        context = WeekContext.from_date(target_date)
        week = self.schedule.get_week(context.type_of_week)
        return week

    def get_lessons_for_day(self, today: date) -> List[LessonModel]:
        context = WeekContext.from_date(today)
        week = self.schedule.get_week(context.type_of_week)

        day_index = today.weekday()
        day_enum = list(DayOfWeekEnum)[day_index]

        day_model: DayModel = next(d for d in week.days if d.day == day_enum)
        return day_model.lessons

    def get_format_schedule_by_week(self, target_date: date) -> str:
        context = WeekContext.from_date(target_date)
        week = self.schedule.get_week(context.type_of_week)

        text = f"Тиждень: {html.bold(week.label)}\n\n"
        for day in week.days:
            text += f"{html.bold(day.label)}\n"
            for lesson in day.lessons:
                text += f"{html.italic(lesson.start_time.strftime('%H:%M'))} - {lesson.subject} "
                text += get_formatted_lesson_links(lesson)
            text += "\n"

        return text

    def build_week_events(self, today: date) -> list[LessonEvent]:
        context = WeekContext.from_date(today)
        week = self.schedule.get_week(context.type_of_week)

        events: list[LessonEvent] = []

        for day in week.days:
            lesson_date: date = context.week_start_date + timedelta(days=DAY_OFFSET[day.day])

            for lesson in day.lessons:
                start_at = datetime.combine(
                    lesson_date,
                    lesson.start_time,
                    tzinfo=ZoneInfo("Europe/Kyiv")
                )

                events.append(LessonEvent(
                    start_at=start_at,
                    title=lesson.subject,
                    zoom=lesson.zoom,
                    zoom_2=lesson.zoom_2,
                    auditory=lesson.auditory,
                    is_online=lesson.is_online,
                    type_lesson=lesson.type_lesson
                ))

        return events

    async def get_format_lesson(self, target_date: date, is_current: bool) -> str:
        lessons: list[LessonModel] = self.get_lessons_for_day(target_date)
        now: time = datetime.now(ZoneInfo(settings.timezone)).time()

        alert_status = await self.alert_service.is_air_raid_active(settings.alert_api_region_uid)
        alert_message = (f"\n\nТривога!"
                         if alert_status
                         else "\n\nТривоги немає")

        response_text = "На поточний момент занять немає"
        response_text += alert_message

        for lesson in lessons:
            if is_current:
                if lesson.start_time <= now <= lesson.end_time:
                    text = html.bold("Поточне заняття:\n\n")
                    text += (
                        f"{html.bold(lesson.subject)}\n"
                        f"{html.italic(lesson.start_time.strftime('%H:%M'))}"
                        f" - {html.italic(lesson.end_time.strftime('%H:%M'))} "
                    )
                    text += get_formatted_lesson_links(lesson)
                    text += "\n\n"
                    text += alert_message
                    return text
            else:
                if lesson.start_time > now:
                    text = html.bold("Наступне заняття:\n\n")
                    text += (
                        f"{html.bold(lesson.subject)}\n"
                        f"{html.italic(lesson.start_time.strftime('%H:%M'))}"
                        f" - {html.italic(lesson.end_time.strftime('%H:%M'))} "
                    )
                    text += get_formatted_lesson_links(lesson)
                    text += "\n\n"
                    text += alert_message
                    return text

        return response_text
