from datetime import timedelta, datetime
from zoneinfo import ZoneInfo

from src.config import settings
from src.model import ScheduleModel, WeekModel, TypeOfWeekEnum, DayOfWeekEnum
from src.model.NotificationEvent import NotificationStatusEnum, NotificationEvent
from src.utils import json_utils
from src.utils.WeekContextResolver import week_context_resolver

DAY_OFFSET = {
    DayOfWeekEnum.monday: 0,
    DayOfWeekEnum.tuesday: 1,
    DayOfWeekEnum.wednesday: 2,
    DayOfWeekEnum.thursday: 3,
    DayOfWeekEnum.friday: 4,
    DayOfWeekEnum.saturday: 5,
    DayOfWeekEnum.sunday: 6,
}


def processing_schedule_json() -> ScheduleModel:
    raw_schedule = json_utils.open_json(settings.path_to_schedule_file)
    schedule: ScheduleModel = json_utils.validate_schedule(raw_schedule)
    return schedule


def add_lesson_notification() -> list[NotificationEvent]:
    events: list[NotificationEvent] = []

    schedule: ScheduleModel = processing_schedule_json()
    week_context = week_context_resolver()

    weeks = schedule.weeks

    weeks_by_type: dict[TypeOfWeekEnum, WeekModel] = {
        w.typeOfWeek: w
        for w in weeks
    }

    current_week: WeekModel = weeks_by_type.get(week_context.type_of_week)

    for day in current_week.days:
        lesson_date = week_context.week_start_date + timedelta(days=DAY_OFFSET[day.day])
        for lesson in day.lessons:
            lesson_start_time = lesson.start_time
            subject = lesson.subject
            notification_status = NotificationStatusEnum.pending

            lesson_start = datetime.combine(lesson_date, lesson_start_time, tzinfo=ZoneInfo("Europe/Kyiv"))
            notify_at = lesson_start - timedelta(minutes=5)

            now = datetime.now(ZoneInfo("Europe/Kyiv"))

            if notify_at <= now:
                continue

            events.append(NotificationEvent(notify_at=notify_at,
                                            lesson_start=lesson_start,
                                            subject=subject,
                                            status=notification_status))

    return events



