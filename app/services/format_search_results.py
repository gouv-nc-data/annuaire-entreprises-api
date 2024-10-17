import json

from app.models.entreprise import (
    EntrepriseResponse,
)

from app.services.formatters.nom_complet import format_nom_complet
from app.services.formatters.adresse_complete import format_adresse_complete


def format_single_entreprise(result, search_params):
    result_entreprise = result["entreprise"]

    def get_field(field, default=None):
        value = result_entreprise.get(field, default)
        if value is None:
            return default
        return value

    entreprise_fields = {
        "ridet": get_field("rid"),
        "nom_complet": format_nom_complet(
            get_field("enseigne"),
            get_field("sigle"),
        ),
        "enseigne": get_field("enseigne"),
        "sigle": get_field("sigle"),
        "adresse_complete": format_adresse_complete(
            get_field("adresse"),
            get_field("ville"),
            get_field("code_postal"),
        ),
        "adresse": get_field("adresse"),
        "ville": get_field("ville"),
        "code_postal": get_field("code_postal"),
        "forme_juridique": get_field("forme_juridique"),
    }

    formatted_entreprise = EntrepriseResponse(**entreprise_fields)

    return formatted_entreprise


def format_search_results(results, search_params):
    """Main formatting function for all results."""
    formatted_results = []
    for result in results:

        print('result in formar search results : ', result)
        # If structure is entreprise
        if "entreprise" in result:
            formatted_result = format_single_entreprise(result, search_params)
            formatted_results.append(formatted_result)
    return formatted_results
