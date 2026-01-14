from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent
PATH_TO_SCHEDULE_FILE = BASE_DIR / "data" / "schedule.json"
PATH_TO_CONSULTATIONS_FILE = BASE_DIR / "data" / "consultation.json"


class Settings(BaseSettings):
    path_to_schedule_file: Path = PATH_TO_SCHEDULE_FILE
    path_to_consultations_file: Path = PATH_TO_CONSULTATIONS_FILE
    bot_token: str

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_file_encoding="utf-8")


settings = Settings()
