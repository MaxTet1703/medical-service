import pydantic_settings
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

from .auth import AuthSettings
from .database import PostgresSettings
from .redis import RedisSettings
from .s3 import S3Config


class Settings(
    AuthSettings,
    PostgresSettings,
    RedisSettings,
    S3Config,
):
    """Settings class for app."""

    model_config = pydantic_settings.SettingsConfigDict(
        env_file="config/.env",
    )


()
settings = Settings(
    Base=declarative_base(),
)
settings.engine = create_async_engine(url=settings.database_url)

settings.session_factory = async_sessionmaker(
    bind=settings.engine,
    expire_on_commit=False,
)
