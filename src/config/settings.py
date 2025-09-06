import os

from pydantic_settings import BaseSettings, SettingsConfigDict

from .app import RunConfig, ApiPrefixConfig, SeedingConfig
from .database import DatabaseConfig
from .storage import AppStorageConfig


class Settings(BaseSettings):
    """Модель настройки приложения"""

    model_config = SettingsConfigDict(
        env_file=os.getenv("APP_ENV_FILE", ".env"),
        extra="ignore",  # Игнорирование посторонних переменных
        case_sensitive=False,
        env_nested_delimiter="__",
        # env_nested_max_split=1,  # Максимальная вложенность настроек - 2
    )
    run: RunConfig = RunConfig()
    api: ApiPrefixConfig = ApiPrefixConfig()
    db: DatabaseConfig = DatabaseConfig()
    storage: AppStorageConfig = AppStorageConfig()
    seeding: SeedingConfig = SeedingConfig()
