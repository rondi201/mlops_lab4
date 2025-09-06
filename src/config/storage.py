from pydantic import BaseModel, Field

from src.core.storage.local import LocalStorageConfig


class StorageConfig(BaseModel):
    backend: str = Field(default="local", description="Тип реализации хранилища")
    """ Тип реализации хранилища """
    local: LocalStorageConfig = Field(
        default_factory=LocalStorageConfig, description="Параметры локального хранилища"
    )
    """ Параметры локального хранилища """


class AppStorageConfig(BaseModel):
    """Настройки путей для хранения объектов"""

    datasets: StorageConfig = Field(
        default=StorageConfig(
            backend="local", local=LocalStorageConfig(mounted_dir="data/datasets")
        ),
        description="Параметры хранилища для набора данных",
    )
    """ Параметры хранилища для набора данных """
    weights: StorageConfig = Field(
        default=StorageConfig(
            backend="local", local=LocalStorageConfig(mounted_dir="data/weights")
        ),
        description="Параметры хранилища для весов обученных моделей",
    )
    """ Параметры хранилища для весов обученных моделей """
