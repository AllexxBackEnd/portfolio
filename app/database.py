from typing import Annotated, Generator

from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column, sessionmaker

# Строка подключения для SQLite
DATABASE_URL = "sqlite:///portfolio.db"

# Создаём Engine
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

# Аннотированные типы для переиспользования в моделях
str_100 = Annotated[str, mapped_column(String(100))]
str_200 = Annotated[str, mapped_column(String(200))]
str_500 = Annotated[str, mapped_column(String(500))]


class Base(DeclarativeBase):
    pass


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
