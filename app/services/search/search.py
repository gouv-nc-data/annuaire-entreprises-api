from app.database.connection import SessionLocal
from app.database import models

db = SessionLocal()


def search(search_params):
    print("search params : ", search_params)

    items = db.query(models.Entreprise).limit(10).all()

    print("items :", items)

    return items
