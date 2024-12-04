from sqlalchemy import or_
from app.database import models
from app.controllers.search_params_model import SearchParams


def search_by_text(search_params: SearchParams):

    query_terms = search_params.terms

    Entreprise = models.Entreprise
    Dirigeant = models.Dirigeant
    Etablissement = models.Etablissement

    return or_(
        Entreprise.designation.icontains(query_terms),
        Entreprise.sigle.icontains(query_terms),
        Entreprise.adresse_physique.icontains(query_terms),
        Dirigeant.nom.icontains(query_terms),
        Etablissement.designation.icontains(query_terms),
        Etablissement.enseigne.icontains(query_terms),
        Etablissement.adresse_physique.icontains(query_terms),
    )
