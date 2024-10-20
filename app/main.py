import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from alembic import command
from alembic.config import Config
from app.database import models
from app.database.connection import engine
from app.exceptions.exception_handlers import add_exception_handlers
from app.routers import public

log = logging.getLogger("uvicorn")


def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


@asynccontextmanager
async def lifespan(app_: FastAPI):
    log.info("Starting up...")
    log.info("run alembic upgrade head...")
    run_migrations()
    yield
    log.info("Shutting down...")


app = FastAPI(
    title="API Recherche d'entreprises | Gouv.nc",
    version="0.0.1",
    contact={
        "name": "Direction du numérique et de la modernisation",
        "url": "https://numerique.gouv.nc/",
        "email": "data@gouv.nc",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    lifespan=lifespan,
)

models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(public.router, prefix="/api/v1")

# Add exception handlers
add_exception_handlers(app)
