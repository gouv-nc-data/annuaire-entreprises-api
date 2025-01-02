import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from alembic import command
from alembic.config import Config
import yaml

from app.database import models
from app.database.connection import engine, url

from app.config import settings

# from app.logging import setup_sentry
from app.exceptions.exception_handlers import add_exception_handlers
from app.routers import public
from app.routers import private
from app.routers import agent_public

# ROOT_LEVEL = "DEBUG"

# LOGGING_CONFIG = {
#     "version": 1,
#     "disable_existing_loggers": True,
#     "formatters": {
#         "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
#     },
#     "handlers": {
#         "default": {
#             "level": "INFO",
#             "formatter": "standard",
#             "class": "logging.StreamHandler",
#             "stream": "ext://sys.stdout",  # Default is stderr
#         },
#     },
#     "loggers": {
#         "": {  # root logger
#             "level": ROOT_LEVEL,
#             "handlers": ["default"],
#             "propagate": False,
#         },
#         "uvicorn.error": {
#             "level": "DEBUG",
#             "handlers": ["default"],
#         },
#         "uvicorn.access": {
#             "level": "DEBUG",
#             "handlers": ["default"],
#         },
#         "alembic": {
#             "level": "DEBUG",
#             "handlers": ["default"],
#         },
#     },
# }

# logging.config.dictConfig(LOGGING_CONFIG)
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

log = logging.getLogger(__name__)


def run_migrations():
    try:
        alembic_cfg = Config("alembic.ini")
        alembic_cfg.set_main_option(
            "sqlalchemy.url", str(url.render_as_string(hide_password=False))
        )
        command.upgrade(alembic_cfg, "head")
    except Exception as e:
        print(e)
        raise e


@asynccontextmanager
async def lifespan(app_: FastAPI):
    log.info("Starting up...")
    log.info("run alembic upgrade head...")
    run_migrations()
    yield
    log.info("Shutting down...")


# Load OpenAPI YAML file
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    with open(settings.openapi.doc_path) as file:
        openapi_schema = yaml.safe_load(file)
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FastAPI(
    title="API Recherche d'entreprises | Gouv.nc",
    version="0.0.1",
    contact={
        "name": "Direction du numérique et de la modernisation",
        "url": "https://data.gouv.nc/",
        "email": "data@gouv.nc",
    },
    license_info={
        "name": "Licence Ouverte v2.0",
        "url": "https://www.etalab.gouv.fr/wp-content/uploads/2017/04/ETALAB-Licence-Ouverte-v2.0.pdf",
    },
    lifespan=lifespan,
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)
print(settings)
app.openapi = custom_openapi

# if Settings.env == "production":
#     setup_sentry()

models.Base.metadata.create_all(bind=engine)


# Include routers
app.include_router(public.router, prefix="/api/v1")
app.include_router(private.router, prefix="/api/v1")
app.include_router(agent_public.router, prefix="/api/v1")

# Add exception handlers
add_exception_handlers(app)
