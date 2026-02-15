from pydantic import BaseModel, Field, ConfigDict


class ProjectCreate(BaseModel):
    """
    Модель для создания и обновления проекта.
    Используется в POST и PUT запросах.
    """

    name_en: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Название проекта на английском (3-100 символов)",
    )
    name_ru: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Название проекта на русском (3-100 символов)",
    )
    description_en: str | None = Field(
        None, max_length=500, description="Описание проекта на английском"
    )
    description_ru: str | None = Field(
        None, max_length=500, description="Описание проекта на русском"
    )
    image_url: str | None = Field(
        None, max_length=200, description="URL скриншота проекта"
    )
    live_url: str | None = Field(
        None, max_length=200, description="Ссылка на живой сайт"
    )
    bot_url: str | None = Field(
        None, max_length=200, description="Ссылка на Telegram бота"
    )
    github_url: str | None = Field(
        None, max_length=200, description="Ссылка на GitHub репозиторий"
    )
    technologies: str | None = Field(
        None,
        max_length=500,
        description="Технологии через запятую (например: FastAPI, PostgreSQL, Redis)",
    )
    project_type: str = Field(
        ...,
        pattern="^(site|bot)$",
        description="Тип проекта: 'site' или 'bot'",
    )


class Project(BaseModel):
    """
    Модель для ответа с данными проекта.
    Используется в GET-запросах.
    """

    id: int = Field(..., description="Уникальный идентификатор проекта")
    name_en: str = Field(..., description="Название проекта на английском")
    name_ru: str = Field(..., description="Название проекта на русском")
    description_en: str | None = Field(None, description="Описание на английском")
    description_ru: str | None = Field(None, description="Описание на русском")
    image_url: str | None = Field(None, description="URL скриншота проекта")
    live_url: str | None = Field(None, description="Ссылка на живой сайт")
    bot_url: str | None = Field(None, description="Ссылка на Telegram бота")
    github_url: str | None = Field(None, description="Ссылка на GitHub репозиторий")
    technologies: str | None = Field(None, description="Технологии через запятую")
    project_type: str = Field(..., description="Тип проекта: 'site' или 'bot'")
    is_active: bool = Field(..., description="Активность проекта")

    model_config = ConfigDict(from_attributes=True)
