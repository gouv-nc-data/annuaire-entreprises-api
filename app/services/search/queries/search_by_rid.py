from sqlalchemy import or_
from app.database import models


def search_by_rid(rid: str):

    Entreprise = models.Entreprise
    Etablissement = models.Etablissement

    return or_(Entreprise.rid == rid, Etablissement.rid == rid)
