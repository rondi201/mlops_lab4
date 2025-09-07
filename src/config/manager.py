from functools import cache

from .app import RunConfig, ApiPrefixConfig, SeedingConfig
from .database import DatabaseConfig
from .storage import StorageConfig
from .settings import Settings


class ConfigManager:
    """
    Класс для получения конфигураций различных частей приложения

    Обёртка над BaseSettings без необходимости создания экземпляра класса настроек сразу,
    что позволяет исбежать ошибок, если происходит импорт компонента без потенциального запуска приложения.
    """

    APP_ENV_PREFIX: str = "APP_"

    @cache
    def get_settings(self) -> Settings:
        """Получить полные настройки приложения"""
        Settings.model_config
        return Settings(_env_prefix=self.APP_ENV_PREFIX)  # type: ignore

    @property
    def api_config(self) -> ApiPrefixConfig:
        return self.get_settings().api

    @property
    def run_config(self) -> RunConfig:
        return self.get_settings().run

    @property
    def db_config(self) -> DatabaseConfig:
        return self.get_settings().db

    @property
    def datasets_storage_config(self) -> StorageConfig:
        return self.get_settings().storage.datasets

    @property
    def weights_storage_config(self) -> StorageConfig:
        return self.get_settings().storage.weights

    @property
    def seeding_config(self) -> SeedingConfig:
        return self.get_settings().seeding
