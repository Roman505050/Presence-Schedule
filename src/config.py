from pydantic_settings import BaseSettings
from datetime import timedelta

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    TELEGRAM_TOKEN: str

    ACTIVE_TO: timedelta = timedelta(hours=2)
    TIMEZONE: str = 'Europe/Kiev'

    @property
    def db_uri_asyncpg(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()