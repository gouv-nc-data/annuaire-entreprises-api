from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from app.database import models

from app.controllers.search_params_model import SearchParams
import logging

log = logging.getLogger(__name__)


def execute_sqlalchemy_query(db: Session, search_client, search_params: SearchParams):

    Entreprise = models.Entreprise
    Dirigeant = models.Dirigeant
    Etablissement = models.Etablissement
    IndicateursFinanciers = models.IndicateursFinanciers
    DepotActe = models.DepotActe

    try:
        stmt = (
            select(Entreprise)
            .join(Dirigeant, Entreprise.id == Dirigeant.entreprise_id, isouter=True)
            .join(
                Etablissement,
                Entreprise.id == Etablissement.entreprise_id,
                isouter=True,
            )
            .join(
                IndicateursFinanciers,
                Entreprise.id == IndicateursFinanciers.entreprise_id,
                isouter=True,
            )
            .join(
                DepotActe,
                Entreprise.id == DepotActe.entreprise_id,
                isouter=True,
            )
            .distinct(Entreprise.id)
            .options(joinedload("*"))
        )

        if search_client is not None:
            stmt = stmt.filter(search_client)

        total_results = 1

    except Exception as e:
        log.error("something went wrong in sql alchemy searching...", e)
        raise e
    finally:
        return {
            "total_results": total_results,
            "results": db.scalars(stmt).unique().all(),
        }
