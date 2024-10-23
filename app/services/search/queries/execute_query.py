from sqlalchemy import or_
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

    query = db.query(Entreprise).filter(query)
    total_results = query.count()
    final_query = query.offset(offset).limit(per_page).distinct()

    for key, value in search_params:
        if key == "code_postal":
            for i in value:
                print('i',i)
                query = query.filter(Entreprise.code_postal == '98461')

    print('query :', query)

    return {"total_results": total_results, "results": query.offset(offset).limit(per_page).distinct().all()}
