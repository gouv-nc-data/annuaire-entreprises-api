from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.exceptions.exception_handlers import add_exception_handlers
from app.exceptions.exceptions import (
    NotFoundError,
)

from app.database.connection import engine
from app.database import models
from app.routers import public

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
)

models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(public.router,prefix='/api/v1')

# Add exception handlers
add_exception_handlers(app)

