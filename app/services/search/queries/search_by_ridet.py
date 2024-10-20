from app.database import models
from app.database.connection import SessionLocal

db = SessionLocal()


def search_by_ridet(searchParams):
    # is_ridet = is_ridet()
    total_results = 10
    items = db.query(models.Entreprise).limit(total_results).all()
    

    results = []

    for item in items:
        results.append({"entreprise": item.__dict__})

    return results
