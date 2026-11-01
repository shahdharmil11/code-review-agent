from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://user:password@postgres:5432/codereviewer"
    redis_url: str = "redis://redis:6379/0"

    class Config:
        env_file = ".env"
