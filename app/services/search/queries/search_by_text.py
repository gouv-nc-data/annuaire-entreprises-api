from sqlalchemy import or_
from app.database import models
from app.controllers.search_params_model import SearchParams


def search_by_text(search_params: SearchParams):

    query_terms = search_params.terms

    Entreprise = models.Entreprise

    return or_(
        Entreprise.designation.icontains(query_terms),
        Entreprise.enseigne.icontains(query_terms),
        Entreprise.adresse_physique.icontains(query_terms),
    )
