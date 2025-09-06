import typing
from .. import AbstractStorageInfo

if typing.TYPE_CHECKING:
    from .storage import LocalStorage, LocalStorageConfig


class LocalStorageInfo(AbstractStorageInfo):
    @property
    def storage_type(self) -> type["LocalStorage"]:
        from .storage import LocalStorage

        return LocalStorage

    @property
    def storage_config_model(self) -> type[LocalStorageConfig]:
        from .configs import LocalStorageConfig

        return LocalStorageConfig
