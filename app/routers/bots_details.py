from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.projects import Project
from app.schemas import ProjectCreate
from app.schemas import Project as ProjectSchema


router = APIRouter(
    prefix="/bots",
    tags=["bots"],
)


@router.get("/", response_model=list[ProjectSchema])
async def get_all_bots(db: Session = Depends(get_db)):
    """
    Возвращает список всех активных Telegram ботов.
    """
    stmt = select(Project).where(
        Project.project_type == "bot",
        Project.is_active == True,
    )
    bots = db.scalars(stmt).all()
    return bots


@router.post("/", response_model=ProjectSchema, status_code=201)
async def create_bot(project_data: ProjectCreate, db: Session = Depends(get_db)):
    """
    Создаёт новый Telegram бот проект.
    """
    project = Project(**project_data.model_dump())
    project.project_type = "bot"
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.get("/{bot_id}", response_model=ProjectSchema)
async def get_bot(bot_id: int, db: Session = Depends(get_db)):
    """
    Возвращает детальную информацию о боте по его ID.
    """
    stmt = select(Project).where(
        Project.id == bot_id,
        Project.project_type == "bot",
    )
    bot = db.scalars(stmt).first()
    if not bot:
        raise HTTPException(status_code=404, detail="Бот не найден")
    return bot


@router.put("/{bot_id}", response_model=ProjectSchema)
async def update_bot(
    bot_id: int, project_data: ProjectCreate, db: Session = Depends(get_db)
):
    """
    Обновляет бот-проект по его ID.
    """
    stmt = select(Project).where(
        Project.id == bot_id,
        Project.project_type == "bot",
    )
    bot = db.scalars(stmt).first()
    if not bot:
        raise HTTPException(status_code=404, detail="Бот не найден")

    for key, value in project_data.model_dump(exclude={"project_type"}).items():
        setattr(bot, key, value)

    db.commit()
    db.refresh(bot)
    return bot


@router.delete("/{bot_id}", status_code=204)
async def delete_bot(bot_id: int, db: Session = Depends(get_db)):
    """
    Удаляет бот-проект по его ID.
    """
    stmt = select(Project).where(
        Project.id == bot_id,
        Project.project_type == "bot",
    )
    bot = db.scalars(stmt).first()
    if not bot:
        raise HTTPException(status_code=404, detail="Бот не найден")

    db.delete(bot)
    db.commit()
