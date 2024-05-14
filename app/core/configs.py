from typing import Any
from pydantic_settings import BaseSettings, SettingsConfigDict
from decouple import config
from sqlalchemy.orm import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """

    model_config = SettingsConfigDict(case_sensitive=True, extra="forbid")

    API_V1_STR: str = "/api/v1"
    TEST_MODE: bool = config("TEST_MODE", default=False, cast=bool)
    DB_URL: str = config("DB_URL_TEST") if TEST_MODE else config("DB_URL")
    DB_BASE_MODEL: Any = declarative_base()
    SECRET_KEY: str = config("SECRET_KEY", default="")
    ALGORITHM: str = config("ALGORITHM", default="")


settings = Settings()
