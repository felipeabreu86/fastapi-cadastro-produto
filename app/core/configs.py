from pydantic_settings import BaseSettings, SettingsConfigDict
from decouple import config


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """

    model_config = SettingsConfigDict(case_sensitive=True, extra="forbid")

    API_V1_STR: str = "/api/v1"
    DB_URL: str = config("DB_URL", default="")


settings = Settings()
