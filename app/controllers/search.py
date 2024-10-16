from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.database import models

db = SessionLocal()


def search(request):
    print("request controller : ", request)

    print('db :', db)

    items = db.query(models.UniteLegale).all()

    print('items : ', items)

    return "ok"
