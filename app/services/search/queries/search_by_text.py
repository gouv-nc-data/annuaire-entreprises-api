from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.database import models


def search_by_text(db: Session, search_params: str):

    query_terms = search_params.terms

    Entreprise = models.Entreprise

    return (
        db.query(Entreprise)
        .filter(
            or_(
                Entreprise.sigle.icontains(query_terms),
                Entreprise.enseigne.icontains(query_terms),
                Entreprise.adresse.icontains(query_terms),
            )
        )
        .distinct()
        .all()
    )
