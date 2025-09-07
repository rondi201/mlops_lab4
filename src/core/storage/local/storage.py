import shutil
from os import PathLike
from typing import BinaryIO
from pathlib import Path, PurePosixPath

from ..abstract import AbstractStorage
from .configs import LocalStorageConfig


class LocalStorage(AbstractStorage):
    """Класс для работы с файлами в локальном хранилище"""

    def __init__(self, mounted_dir: str | PathLike):
        """
        Инициализация класса

        Args:
            mounted_dir (PathLike): Директория, в которой будут храниться файлы
        """
        self._mounted_dir = Path(mounted_dir)

    @classmethod
    def from_config(cls, settings: LocalStorageConfig) -> "LocalStorage":
        return cls(mounted_dir=settings.mounted_dir)

    def connect(self):
        # Подключение к локальному хранилищу не требуется
        pass

    def upload(
        self,
        file: str | PathLike | BinaryIO | bytes,
        save_dir: str | None = None,
        name: str | None = None,
        exsist_ok: bool = False,
    ) -> str:
        # Получим имя файла для сохранения
        save_name = name or getattr(file, "name")
        # Если имя не задано и файл не содержит имени - ошибка
        if not save_name:
            raise RuntimeError(
                f"Passed 'file' object ({type(file)}) does not provide name or 'name' is empty. "
                f"Set 'name' manually"
            )

        # Сформируем путь для сохранения
        save_path = str(PurePosixPath(save_dir or "", save_name))
        absolute_save_path = self._mounted_dir / save_path
        absolute_save_path.parent.mkdir(parents=True, exist_ok=True)

        # Проверим на существование файла
        if not exsist_ok and absolute_save_path.exists():
            raise FileExistsError(f"File {save_path} already exists.")

        # Скопируем на диск, если это другой файл
        if isinstance(file, (str, PathLike)):
            shutil.copy2(file, absolute_save_path)
        # Иначе - запишем в файл
        else:
            # Получим сырые данные
            if isinstance(file, BinaryIO):
                raw_data = file.read()
            else:
                raw_data = file
            # Сохраним файл на диск
            with open(absolute_save_path, "wb") as f:
                f.write(raw_data)

        return save_path

    def download(self, link: str) -> tuple[bytes, str]:
        # Получим путь для считывания файла
        absolute_save_path = self._mounted_dir / link
        # Если файла не существует - ошибка
        if not absolute_save_path.exists():
            raise FileNotFoundError(f"File with link {link} not found")
        # Считаем файл
        with open(absolute_save_path, "rb") as f:
            raw_data = f.read()
        return raw_data, absolute_save_path.name

    def delete(self, link: str):
        # Получим путь для удаления файла
        absolute_save_path = self._mounted_dir / link
        # Если файла не существует - ошибка
        if not absolute_save_path.exists():
            raise FileNotFoundError(f"File with link {link} not found")
        # Удаляем файл
        absolute_save_path.unlink()

    def exists(self, link: str) -> bool:
        # Получим путь до файла
        absolute_save_path = self._mounted_dir / link
        # Проверим существование файла
        return absolute_save_path.exists()

    def close(self):
        # Закрытие подключения не требуется
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(mounted_dir={self._mounted_dir})"
