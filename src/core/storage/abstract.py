from abc import ABC, abstractmethod
from io import BytesIO
from os import PathLike
from typing import BinaryIO

from pydantic import BaseModel


class BaseStorageConfig(BaseModel):
    """Модель настроек модуля для работы с хранилищем"""

    pass


class AbstractStorage(ABC):
    """Класс для работы с файлами в абстрактном хранилище"""

    @classmethod
    @abstractmethod
    def from_config(cls, settings: BaseStorageConfig) -> "AbstractStorage":
        """Инициализация модуля из настроек"""
        pass

    @abstractmethod
    def connect(self):
        """Инициализация состояний и подключения к хранилищу"""
        pass

    @abstractmethod
    def upload(
        self,
        file: str | PathLike | BinaryIO | BytesIO | bytes,
        save_dir: str | None = None,
        name: str | None = None,
        exsist_ok: bool = False,
    ) -> str:
        """
        Загрузка файла в хранилище

        Args:
            file (str | PathLike | BinaryIO | bytes): путь до файла на диске или
                BinaryIO | BytesIO | bytes объект для считывания
            save_dir (str | None): целевая директория для сохранения. Если не задано - сохраняется на усмотрение
                имплементирующего класса
            name (str | None): имя файла, под которым он будет сохранён. Если не задано - возьмётся имя текущего объекта
            exsist_ok (bool): если True - перезаписывает существующий файл, иначе - вызовет ошибку, если файл уже существует

        Returns:
            (str): ссылка на файл, доступ к которому может быть получен через метод `download`
        """
        pass

    @abstractmethod
    def download(self, link: str) -> tuple[bytes, str]:
        """
        Скачивание файла из хранилища

        Args:
            link (str): ссылка на файл, полученная от метода `upload`
        Returns:
            (bytes, str): кортеж (data, name), где data - файл, полученный по ссылке; name - имя файла

        Raise:
            FileNotFoundError: если файл не найден
            ValueError: если формат ссылки не корректен
        """
        pass

    @abstractmethod
    def delete(self, link: str):
        """
        Удаление файла из хранилища

        Args:
            link (str): ссылка на файл, полученная от метода `upload`

        Raise:
            FileNotFoundError: если файл не найден
            ValueError: если формат ссылки не корректен
        """
        pass

    @abstractmethod
    def exists(self, link: str) -> bool:
        """
        Проверка на существования файла в хранилище

        Args:
            link (str): ссылка на файл, полученная от метода `upload`
        Returns:
            (bool): Существует ли файл в хранилище

        Raise:
            ValueError: если формат ссылки не корректен
        """
        pass

    @abstractmethod
    def close(self):
        """Сброс состояний, подключения и высвобождение ресурсов"""
        pass


class AbstractStorageInfo(ABC):
    @property
    @abstractmethod
    def storage_type(self) -> type[AbstractStorage]:
        pass

    @property
    @abstractmethod
    def storage_config_model(self) -> type[BaseStorageConfig]:
        pass
