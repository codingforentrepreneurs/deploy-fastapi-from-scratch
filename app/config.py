import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Fastapi APP"
    app_db: str = os.environ.get("APP_DB") or None

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()