from app.controllers.search_params_model import SearchParams


def search_by_text(search_params: SearchParams):

    query_terms = search_params.terms

    search_parameters = {
        "q": query_terms,
        "query_by": "designation, sigle, etablissements.enseigne, adresse_physique, etablissements.adresse_physique, dirigeants.nom, dirigeants.prenoms",
        "sort_by": "etat_rid:asc",
    }

    return search_parameters
