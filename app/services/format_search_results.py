from app.models.unite_legale import UniteLegaleResponse
from app.services.formatters.adresse_complete import format_adresse_complete
from app.services.formatters.indicateurs_financiers import format_indicateurs_financiers
from app.services.formatters.depot_acte import format_depot_acte
from app.services.formatters.nom_complet import format_nom_complet
from app.services.formatters.date import format_date
from app.services.formatters.dirigeants import format_dirigeants
from app.services.formatters.etablissements import format_etablissements
import logging

log = logging.getLogger(__name__)


def format_single_entreprise(result, search_params):
    result_entreprise = result["entreprise"]

    log.debug("result_entreprise", result_entreprise)

    def get_field(field, default=None):
        value = result_entreprise.get(field, default)
        if value is None:
            return default
        return value

    entreprise_fields = {
        "rid": get_field("rid"),
        "nom_complet": format_nom_complet(
            get_field("designation"),
            get_field("sigle"),
        ),
        "sigle": get_field("sigle"),
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
        "etat_rid": get_field("etat_rid"),
        # Relations
        "etablissements": format_etablissements(get_field("etablissements")),
        "dirigeants": format_dirigeants(get_field("dirigeants")),
        "indicateurs_financiers": format_indicateurs_financiers(
            get_field("indicateurs_financiers")
        ),
        "depot_actes": format_depot_acte(get_field("depot_actes")),
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
