from pydantic import BaseModel, SecretStr, Field


class DatabaseConfig(BaseModel):
    """Конфигурация настройки базы данных"""

    dialect: str = Field(
        default="",
        description="Вид диалекта SQL (см. https://docs.sqlalchemy.org/en/20/core/engines.html)",
    )
    """ Вид диалекта SQL (см. https://docs.sqlalchemy.org/en/20/core/engines.html) """
    host: str = Field(
        default="localhost",
        description="Адрес базы данных",
    )
    """ Адрес базы данных """
    port: int = Field(
        default=5432,
        description="Порт базы данных",
    )
    """ Порт базы данных """
    user: str = Field(
        default="su",
        description="Логин для доступа к базе данных",
    )
    """ Логин для доступа к базе данных """
    password: SecretStr = Field(
        default=SecretStr(""),
        description="Пароль для доступа к базе данных",
    )
    """ Пароль для доступа к базе данных """
    database: str = Field(
        default="app-database",
        description="Имя базы в базе данных",
    )
    """ Имя базы в базе данных """
