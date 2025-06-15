from sqlalchemy import or_
from app.database import models


def search_by_rid(rid: str):

    Entreprise = models.Entreprise

    clean_rid = rid.replace(" ", "")

    if len(clean_rid) == 6:
        clean_rid = "0" + clean_rid

    return or_(Entreprise.rid == clean_rid)
