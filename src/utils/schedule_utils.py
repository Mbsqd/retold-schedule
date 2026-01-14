from datetime import datetime

from aiogram import html

from src.model.schedule import ScheduleModel, TypeOfWeekEnum, WeekModel, DayOfWeekEnum, TypeLessonEnum
from src.utils import json_utils


def processing_json() -> ScheduleModel:
    raw_schedule = json_utils.open_json()
    schedule: ScheduleModel = json_utils.validate_schedule(raw_schedule)
    return schedule


def calculate_current_week_type() -> TypeOfWeekEnum:
    current_date = datetime.today()
    current_week_number = current_date.isocalendar().week
    print(current_week_number)
    if current_week_number % 2 == 0:
        return TypeOfWeekEnum.numerator
    else:
        return TypeOfWeekEnum.denominator


class ScheduleProcessor:
    def __init__(self):
        self.schedule = processing_json()

    schedule: ScheduleModel
    typeCurrentWeek: TypeOfWeekEnum = TypeOfWeekEnum.numerator

    def generate_schedule_message_for_week(self, is_current: bool) -> str:
        schedule = self.schedule
        weeks = schedule.weeks

        weeks_by_type: dict[TypeOfWeekEnum, WeekModel] = {
            w.typeOfWeek: w
            for w in weeks
        }

        current_week_type = calculate_current_week_type()
        if not is_current:
            current_week_type = TypeOfWeekEnum.denominator if current_week_type == TypeOfWeekEnum.numerator else TypeOfWeekEnum.numerator

        current_week: WeekModel = weeks_by_type.get(current_week_type)

        message_text = f"Тиждень: {html.bold(current_week.label)}\n\n"

        for day in current_week.days:
            current_day = day.label.value
            message_text += f"{html.bold(current_day)}\n"
            for lesson in day.lessons:
                message_text += f"{html.italic(lesson.start_time.strftime("%H:%M"))} - {lesson.subject}"
                if lesson.is_online:
                    if lesson.type_lesson.value == TypeLessonEnum.lecture:
                        message_text += f" {html.italic(html.link("Лекція", lesson.zoom))}\n"
                    else:
                        if lesson.zoom_2:
                            message_text += f" {html.italic(html.link("I", lesson.zoom))}"
                            message_text += f" {html.italic(html.link("II", lesson.zoom_2))}\n "
                        else:
                            message_text += f" {html.italic(html.link("Практика", lesson.zoom))}\n"
                else:
                    if lesson.type_lesson.value == TypeLessonEnum.lecture:
                        message_text += f" {html.italic(html.italic("Лекція"))} {html.underline(lesson.auditory)}\n"
                    else:
                        message_text += f" {html.italic(html.italic("Практика"))}: {html.underline(lesson.auditory)}\n"


            message_text += "\n"

        return message_text
