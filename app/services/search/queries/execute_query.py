from sqlalchemy.orm import Session
from app.database import models

from app.controllers.search_params_model import SearchParams


def execute_sqlalchemy_query(db: Session, query, search_params: SearchParams):

    Entreprise = models.Entreprise

    page = search_params.page
    per_page = search_params.per_page
    offset = 0

    if page > 1:
        offset = (page - 1) * per_page

    return {
        "total_results": db.query(Entreprise).filter(query).count(),
        "results": db.query(Entreprise)
        .filter(query)
        .offset(offset)
        .limit(per_page)
        .distinct()
        .all(),
    }
