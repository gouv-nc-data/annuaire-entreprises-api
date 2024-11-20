from app.models.unite_legale import UniteLegaleResponse
from app.services.formatters.adresse_complete import format_adresse_complete
from app.services.formatters.nom_complet import format_nom_complet
from app.services.formatters.date import format_date


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
            get_field("designation"),
            get_field("enseigne"),
        ),
        "enseigne": get_field("enseigne"),
        "designation": get_field("designation"),
        "adresse_complete": format_adresse_complete(
            get_field("adresse_physique"),
            get_field("ville_physique"),
            get_field("code_postal_physique"),
        ),
        "adresse_physique": get_field("adresse_physique"),
        "ville_physique": get_field("ville_physique"),
        "code_postal_physique": get_field("code_postal_physique"),
        "forme_juridique": get_field("forme_juridique"),
        "ape": get_field("ape"),
        "code_ape": get_field("code_ape"),
        "date_creation": format_date(get_field("date_creation")),
        "date_radiation": format_date(get_field("date_radiation")),
    }

    formatted_entreprise = UniteLegaleResponse(**entreprise_fields)

    return formatted_entreprise


def format_search_results(results, search_params):
    """Main formatting function for all results."""
    formatted_results = []
    for result in results:
        # If structure is entreprise
        if "entreprise" in result:
            formatted_result = format_single_entreprise(result, search_params)
            formatted_results.append(formatted_result)
    return formatted_results
