from sqlalchemy import func
from sqlalchemy.orm import Session
from app.database import models

from app.controllers.search_params_model import SearchParams
from app.controllers.field_validation import VALID_FIELD_VALUES


def execute_sqlalchemy_query(db: Session, query, search_params: SearchParams):

    Entreprise = models.Entreprise

    page = search_params.page
    per_page = search_params.per_page
    offset = 0

    if page > 1:
        offset = (page - 1) * per_page

    try:
        query = db.query(Entreprise).filter(query)

        for key, value in search_params:

            field = VALID_FIELD_VALUES.get(key)

            if isinstance(field, dict):
                alias = field["alias"]
                if alias != None:
                    if value != None:
                        try:
                            filter_expr = func.upper(getattr(Entreprise, alias)).in_(
                                value
                            )
                            query = query.filter(filter_expr)
                        except Exception as e:
                            print("Filtering regex in sql alchemy is wrong...", e)

        total_results = query.count()

    except Exception as e:
        print("something went wrong in sql alchemy searching...", e)
    finally:
        return {
            "total_results": total_results,
            "results": query.offset(offset).limit(per_page).distinct().all(),
        }
