from sqlalchemy.orm import Session
from app.database import models

def search_by_ridet(db: Session, ridet: str):

    Entreprise = models.Entreprise

    return db.query(Entreprise).filter(Entreprise.rid == ridet).all()
