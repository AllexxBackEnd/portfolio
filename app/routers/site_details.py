from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.projects import Project
from app.schemas import ProjectCreate
from app.schemas import Project as ProjectSchema


router = APIRouter(
    prefix="/sites",
    tags=["sites"],
)


@router.get("/", response_model=list[ProjectSchema])
async def get_all_sites(db: Session = Depends(get_db)):
    """
    Возвращает список всех активных веб-проектов.
    """
    stmt = select(Project).where(
        Project.project_type == "site",
        Project.is_active == True,
    )
    sites = db.scalars(stmt).all()
    return sites


@router.post("/", response_model=ProjectSchema, status_code=201)
async def create_site(project_data: ProjectCreate, db: Session = Depends(get_db)):
    """
    Создаёт новый веб-проект.
    """
    project = Project(**project_data.model_dump())
    project.project_type = "site"
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.get("/{site_id}", response_model=ProjectSchema)
async def get_site(site_id: int, db: Session = Depends(get_db)):
    """
    Возвращает детальную информацию о веб-проекте по его ID.
    """
    stmt = select(Project).where(
        Project.id == site_id,
        Project.project_type == "site",
    )
    site = db.scalars(stmt).first()
    if not site:
        raise HTTPException(status_code=404, detail="Сайт не найден")
    return site


@router.put("/{site_id}", response_model=ProjectSchema)
async def update_site(
    site_id: int, project_data: ProjectCreate, db: Session = Depends(get_db)
):
    """
    Обновляет веб-проект по его ID.
    """
    stmt = select(Project).where(
        Project.id == site_id,
        Project.project_type == "site",
    )
    site = db.scalars(stmt).first()
    if not site:
        raise HTTPException(status_code=404, detail="Сайт не найден")

    for key, value in project_data.model_dump(exclude={"project_type"}).items():
        setattr(site, key, value)

    db.commit()
    db.refresh(site)
    return site


@router.delete("/{site_id}", status_code=204)
async def delete_site(site_id: int, db: Session = Depends(get_db)):
    """
    Удаляет веб-проект по его ID.
    """
    stmt = select(Project).where(
        Project.id == site_id,
        Project.project_type == "site",
    )
    site = db.scalars(stmt).first()
    if not site:
        raise HTTPException(status_code=404, detail="Сайт не найден")

    db.delete(site)
    db.commit()
