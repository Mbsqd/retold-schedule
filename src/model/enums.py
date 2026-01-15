from enum import Enum


class TypeOfWeekEnum(str, Enum):
    numerator = "numerator"
    denominator = "denominator"


class DayOfWeekEnum(str, Enum):
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"
    saturday = "saturday"
    sunday = "sunday"


class TypeLessonEnum(str, Enum):
    lecture = "lecture"
    practice = "practice"