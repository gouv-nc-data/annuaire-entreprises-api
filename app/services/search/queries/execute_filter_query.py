from sqlalchemy import func, select
from sqlalchemy.orm import Session, joinedload
from app.database import models

from app.controllers.search_params_model import SearchParams
from app.controllers.field_validation import VALID_FIELD_VALUES
import logging

log = logging.getLogger(__name__)

def execute_sqlalchemy_query(db: Session, search_client, search_params: SearchParams):

    Entreprise = models.Entreprise
    Dirigeant = models.Dirigeant
    Etablissement = models.Etablissement

    page = search_params.page
    per_page = search_params.per_page
    offset = 0

    if page > 1:
        offset = (page - 1) * per_page

    try:
        stmt = (
            select(Entreprise)
            .join(Dirigeant, Entreprise.id == Dirigeant.entreprise_id, isouter=True)
            .join(
                Etablissement,
                Entreprise.id == Etablissement.entreprise_id,
                isouter=True,
            )
            .distinct(Entreprise.id)
            .options(joinedload("*"))
        )

        count_stmt = (
            select(func.count(func.distinct(Entreprise.id)))
            .join(Dirigeant, Entreprise.id == Dirigeant.entreprise_id, isouter=True)
            .join(
                Etablissement,
                Entreprise.id == Etablissement.entreprise_id,
                isouter=True,
            )
            .options(joinedload("*"))
        )

        if search_client is not None:
            stmt = stmt.filter(search_client)
            count_stmt = count_stmt.filter(search_client)

        for key, value in search_params:

            field = VALID_FIELD_VALUES.get(key)

            if isinstance(field, dict):
                alias = field["alias"]
                if alias is not None:
                    if value is not None:
                        try:
                            filter_expr = func.upper(getattr(Entreprise, alias)).in_(
                                value
                            )
                            stmt = stmt.filter(filter_expr)
                            count_stmt = count_stmt.filter(filter_expr)
                        except Exception as e:
                            log.error("Filtering regex in sql alchemy is wrong...", e)
                            raise e

        total_results = db.execute(count_stmt).scalar_one()

    except Exception as e:
        log.error("something went wrong in sql alchemy searching...", e)
        raise e
    finally:
        return {
            "total_results": total_results,
            "results": db.scalars(stmt.offset(offset).limit(per_page)).unique().all(),
        }
