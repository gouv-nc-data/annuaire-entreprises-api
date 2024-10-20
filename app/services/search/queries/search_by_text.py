from app.database import models
from app.database.connection import SessionLocal

db = SessionLocal()


def search_by_text(searchParams):
    # is_ridet = is_ridet()

    items = db.query(models.Entreprise).limit(10).all()

    return items
