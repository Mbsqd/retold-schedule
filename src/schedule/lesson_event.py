from datetime import datetime

from src.schedule.enums import TypeLessonEnum


class LessonEvent:
    def __init__(self,
                 start_at: datetime,
                 title: str,
                 zoom: str | None,
                 zoom_2: str | None,
                 auditory: str | None,
                 is_online: bool,
                 type_lesson: TypeLessonEnum
                 ) -> None:
        self.start_at = start_at
        self.title = title
        self.zoom: str | None = zoom
        self.zoom_2: str | None = zoom_2
        self.auditory = auditory
        self.is_online: bool = is_online
        self.type_lesson: TypeLessonEnum = type_lesson
