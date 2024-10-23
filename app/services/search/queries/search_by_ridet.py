from app.database import models


def search_by_ridet(ridet: str):

    Entreprise = models.Entreprise

    return Entreprise.rid == ridet
