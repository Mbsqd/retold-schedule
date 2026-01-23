from enum import Enum


class MainMenu(str, Enum):
    CURRENT_WEEK = "🗓 Поточний тиждень"
    NEXT_WEEK = "➡️ Наступний тиждень"
    CURRENT_LESSON = "⏰ Поточне заняття"
    NEXT_LESSON = "➡️ Наступне заняття"
    CONSULTATIONS = "🗒 Консультації"
