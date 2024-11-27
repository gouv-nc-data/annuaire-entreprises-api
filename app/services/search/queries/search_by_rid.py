from app.database import models


def search_by_rid(rid: str):

    Entreprise = models.Entreprise

    return Entreprise.rid == rid
