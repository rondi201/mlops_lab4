from os import PathLike
from pydantic import Field

from ..abstract import BaseStorageConfig


class LocalStorageConfig(BaseStorageConfig):
    mounted_dir: str | PathLike = Field(
        default=".cache/files",
        description="Директория, в которой будут храниться файлы",
    )
