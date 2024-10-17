from app.database.connection import SessionLocal
from app.database import models

from app.services.search.parsers.ridet import is_ridet

db = SessionLocal()


def search_by_ridet(searchParams):
    # is_ridet = is_ridet()

    items = db.query(models.Entreprise).limit(10).all()
    total_results = 10

    results = []

    for item in items:
        results.append({"entreprise": item.__dict__})

    return results
