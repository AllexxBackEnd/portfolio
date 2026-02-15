from sqlalchemy import String, Text, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base, str_100, str_200, str_500


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name_en: Mapped[str_100] = mapped_column(String(100))
    name_ru: Mapped[str_100] = mapped_column(String(100))
    description_en: Mapped[str | None] = mapped_column(Text)
    description_ru: Mapped[str | None] = mapped_column(Text)
    image_url: Mapped[str_200 | None] = mapped_column(String(200))
    live_url: Mapped[str_200 | None] = mapped_column(String(200))
    bot_url: Mapped[str_200 | None] = mapped_column(String(200))
    github_url: Mapped[str_200 | None] = mapped_column(String(200))
    technologies: Mapped[str_500 | None] = mapped_column(String(500))
    project_type: Mapped[str] = mapped_column(String(20))  # "site" or "bot"
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
