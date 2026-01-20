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


DAY_OFFSET = {
    DayOfWeekEnum.monday: 0,
    DayOfWeekEnum.tuesday: 1,
    DayOfWeekEnum.wednesday: 2,
    DayOfWeekEnum.thursday: 3,
    DayOfWeekEnum.friday: 4,
    DayOfWeekEnum.saturday: 5,
    DayOfWeekEnum.sunday: 6,
}
