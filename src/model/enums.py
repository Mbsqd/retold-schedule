from enum import Enum


class TypeOfWeekEnum(str, Enum):
    numerator = "numerator"
    denominator = "denominator"


class DayOfWeekEnum(str, Enum):
    monday = "Понеділок"
    tuesday = "Вівторок"
    wednesday = "Середа"
    thursday = "Четвер"
    friday = "П'ятниця"
    saturday = "Субота"
    sunday = "Неділя"


class TypeLessonEnum(str, Enum):
    lecture = "lecture"
    practice = "practice"