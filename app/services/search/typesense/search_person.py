from app.controllers.search_params_model import SearchParams


def search_person(search_params: SearchParams):

    query_terms = search_params.terms
    query_person = search_params.dirigeant

    q = query_person

    if query_terms is not None:
        q = q + " " + query_terms

        search_parameters = {
            "q": q,
            "query_by_weights": "100,1,1,1,1,1",
            "query_by": ", dirigeants.nom, designation, sigle, etablissements.enseigne, adresse_physique, etablissements.adresse_physique",
        }

    else:
        search_parameters = {
            "q": q,
            "query_by": ", dirigeants.nom",
        }


    return search_parameters
