import inspect
import importlib

from .abstract import AbstractStorage, BaseStorageConfig, AbstractStorageInfo


def get_storage_backend_info(backend_name: str) -> AbstractStorageInfo:
    """
    Возвращает информацию о хранилище по типу его реализации

    Args:
        backend_name (str): тип реализации хранилища

    Returns:
        AbstractStorageInfo: Информация о хранилище, реализованная согласно типу
    """
    backend_module = importlib.import_module(f"{__name__}.{backend_name}")

    for name, obj in inspect.getmembers(backend_module):
        print(obj)
        if issubclass(obj, AbstractStorageInfo):
            return obj()

    raise ModuleNotFoundError(
        f"Storage backend with name '{backend_name}' not found. Please check the backend name."
    )
