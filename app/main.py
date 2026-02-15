from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from sqlalchemy.orm import Session
import uvicorn
import glob
import os

from app.routers import site_details
from app.routers import bots_details
from app.database import get_db
from app.models.projects import Project


app = FastAPI(
    title="FastAPI Portfolio",
    version="0.1.0",
)

templates = Jinja2Templates(directory="templates")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(site_details.router)
app.include_router(bots_details.router)


def _get_image_files():
    """Collect all image file paths relative to project root."""
    files = set()
    for path in glob.glob("assets/img/portfolio/*"):
        files.add(path.replace(os.sep, "/"))
    return files


@app.get("/", response_class=HTMLResponse)
async def get_portfolio_page(request: Request, db: Session = Depends(get_db)):
    sites = db.scalars(
        select(Project).where(Project.project_type == "site", Project.is_active == True)
    ).all()
    bots = db.scalars(
        select(Project).where(Project.project_type == "bot", Project.is_active == True)
    ).all()
    image_files = _get_image_files()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "sites": sites, "bots": bots, "image_files": image_files},
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
