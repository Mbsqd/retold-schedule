from src.schedule.enums import TypeLessonEnum
from src.schedule.lesson_event import LessonEvent
from src.schedule.models import LessonModel

from aiogram import html


def get_formatted_lesson_links(lesson: LessonModel | LessonEvent) -> str:
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

# def get_formatted_lesson_links(event: LessonEvent) -> str:
#     text: str = ""
#     if event.is_online:
#         if event.type_lesson == TypeLessonEnum.lecture:
#             text += f"{html.italic(html.link("Лекція", event.zoom))}\n"
#         else:
#             if event.zoom_2:
#                 text += f"{html.italic(html.link("I", event.zoom))} "
#                 text += f"{html.italic(html.link("II", event.zoom_2))}\n"
#             else:
#                 text += f"{html.italic(html.link("Практика", event.zoom))}\n"
#     else:
#         if event.type_lesson == TypeLessonEnum.lecture:
#             text += f"{html.italic("Лекція")} {html.underline(event.auditory)}\n"
#         else:
#             text += f"{html.italic("Практика")}: {html.underline(event.auditory)}\n"
#
#     return text
