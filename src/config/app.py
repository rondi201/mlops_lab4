from pydantic import BaseModel, Field


class RunConfig(BaseModel):
    """Настройки запуска приложения"""

    host: str = Field(
        default="localhost", description="Имя хоста для доступа к приложению"
    )
    """ Имя хоста для доступа к приложению """
    port: int = Field(default=8000, description="Порт для доступа к приложению")
    """ Порт для доступа к приложению """


class ApiPrefixConfig(BaseModel):
    """Настройки путей для доступа к routers"""

    prefix: str = "/api"
    health: str = "/health"
    datasets: str = "/datasets"
    mlmodels: str = "/mlmodels"
    predict: str = "/predict"
    tasks: str = "/tasks"


class SeedingConfig(BaseModel):
    """Настройки автозаполнения базы данных"""

    predict_tasks_seeding_config: str = "data/seed_data/predict_tasks.json"
    datasets_seeding_config: str = "data/seed_data/datasets.json"
    mlmodels_seeding_config: str = "data/seed_data/mlmodels.json"
