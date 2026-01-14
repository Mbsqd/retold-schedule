from datetime import datetime, time
from zoneinfo import ZoneInfo

from aiogram import html

from config import settings
from src.model.schedule import ScheduleModel, WeekModel, DayModel, LessonModel
from src.model.enums import TypeOfWeekEnum, DayOfWeekEnum, TypeLessonEnum
from src.utils import json_utils


def processing_schedule_json() -> ScheduleModel:
    raw_schedule = json_utils.open_json(settings.path_to_schedule_file)
    schedule: ScheduleModel = json_utils.validate_schedule(raw_schedule)
    return schedule


def get_current_week_type() -> TypeOfWeekEnum:
    tz_ua = ZoneInfo("Europe/Kyiv")
    current_date = datetime.now(tz_ua)
    current_week_number = current_date.isocalendar().week
    print(current_week_number)
    if current_week_number % 2 == 0:
        return TypeOfWeekEnum.numerator
    else:
        return TypeOfWeekEnum.denominator


def get_current_week_day() -> DayOfWeekEnum:
    week_day_number = datetime.today().weekday()
    mapping = [
        DayOfWeekEnum.monday,
        DayOfWeekEnum.tuesday,
        DayOfWeekEnum.wednesday,
        DayOfWeekEnum.thursday,
        DayOfWeekEnum.friday,
        DayOfWeekEnum.saturday,
        DayOfWeekEnum.sunday,
    ]
    return mapping[week_day_number]


def get_current_time() -> time:
    return datetime.now(ZoneInfo("Europe/Kyiv")).time()


def get_formatted_lesson_link(lesson: LessonModel) -> str:
    text: str = ""
    if lesson.is_online:
        if lesson.type_lesson == TypeLessonEnum.lecture:
            text += f"{html.italic(html.link("Лекція", lesson.zoom))}\n"
        else:
            if lesson.zoom_2:
                text += f"{html.italic(html.link("I", lesson.zoom))} "
                text += f"{html.italic(html.link("II", lesson.zoom_2))}\n"
            else:
                text += f"{html.italic(html.link("Практика", lesson.zoom))}\n"
    else:
        if lesson.type_lesson == TypeLessonEnum.lecture:
            text += f"{html.italic("Лекція")} {html.underline(lesson.auditory)}\n"
        else:
            text += f"{html.italic("Практика")}: {html.underline(lesson.auditory)}\n"

    return text


class ScheduleProcessor:
    def __init__(self):
        self.schedule = processing_schedule_json()

    schedule: ScheduleModel
    typeCurrentWeek: TypeOfWeekEnum = TypeOfWeekEnum.numerator

    # Если текущая неделя кратна трем, добавить в конце сообщения уведомлени об магической недели
    # (На это недели занятия в субботу)
    def generate_schedule_message_for_week(self, is_current: bool) -> str:
        schedule = self.schedule
        weeks = schedule.weeks

        weeks_by_type: dict[TypeOfWeekEnum, WeekModel] = {
            w.typeOfWeek: w
            for w in weeks
        }

        current_week_type = get_current_week_type()
        if not is_current:
            current_week_type = TypeOfWeekEnum.denominator if current_week_type == TypeOfWeekEnum.numerator else TypeOfWeekEnum.numerator

        current_week: WeekModel = weeks_by_type.get(current_week_type)

        message_text = f"Тиждень: {html.bold(current_week.label)}\n\n"

        for day in current_week.days:
            current_day = day.label.value
            message_text += f"{html.bold(current_day)}\n"
            for lesson in day.lessons:
                message_text += f"{html.italic(lesson.start_time.strftime('%H:%M'))} - {lesson.subject} "
                message_text += get_formatted_lesson_link(lesson)

            message_text += "\n"

        return message_text

    def generate_lesson_message(self, is_current: bool) -> str:
        schedule = self.schedule
        weeks = schedule.weeks

        weeks_by_type: dict[TypeOfWeekEnum, WeekModel] = {
            w.typeOfWeek: w
            for w in weeks
        }

        current_week_type = get_current_week_type()
        current_week: WeekModel = weeks_by_type.get(current_week_type)

        current_week_day_enum = get_current_week_day()
        current_day: DayModel = next(day for day in current_week.days if day.label == current_week_day_enum)

        current_time = get_current_time()

        message_text = f"{html.bold("На поточний момент занять немає")}"

        for lesson in current_day.lessons:
            if is_current:
                if lesson.start_time <= current_time <= lesson.end_time:
                    message_text = (f"{html.bold(lesson.subject)}\n"
                                    f"{html.italic(lesson.start_time.strftime('%H:%M'))} - ")
                    message_text += get_formatted_lesson_link(lesson)
                    break
            else:
                if lesson.start_time > current_time:
                    message_text = (f"{html.bold(lesson.subject)}\n"
                                    f"{html.italic(lesson.start_time.strftime('%H:%M'))} - \n")
                    message_text += get_formatted_lesson_link(lesson)
                    break

        return message_text
