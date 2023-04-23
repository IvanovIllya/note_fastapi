import os
from pathlib import Path
from pydantic import BaseSettings

BASE_DIR = (Path(__file__) / ".." / ".." / ".." / "..").resolve()
ENV_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_HOST: str
    PROJECT_PORT: int

    DB_USER: str
    DB_NAME: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int

    INIT_NOTES: list = [
        {"id": 1, "title": "Правило номер 15", "text": "Сейчас лучше, чем никогда"},
        {"id": 2, "title": "Правило номер 3", "text": "Простое лучше, чем сложное"}
    ]


    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()