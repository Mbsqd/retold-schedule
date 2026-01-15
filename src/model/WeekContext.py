from datetime import date

from pydantic import BaseModel

from src.model import TypeOfWeekEnum


# Добавить поле спец. недели
class WeekContext(BaseModel):
    week_start_date: date
    week_end_date: date
    type_of_week: TypeOfWeekEnum