from app.models.unite_legale import Dirigeant
from app.services.formatters.dirigeant_nom_complet import format_dirigeant_nom_complet
from app.utils.helpers import get_value


def format_dirigeants(dirigeants=None):

    dirigeants_formatted = []

    if dirigeants:
        for dirigeant_data in dirigeants:

            if isinstance(dirigeant_data, dict):
                dirigeant = dirigeant_data
            else:
                dirigeant = dirigeant_data.__dict__

            # We only send active dirigeant
            if not dirigeant["actif"]:
                break

            dirigeant = Dirigeant(
                nom_personne_morale=get_value(dirigeant, "nom_personne_morale"),
                nom=get_value(dirigeant, "nom"),
                prenoms=get_value(dirigeant, "prenoms"),
                nom_complet=format_dirigeant_nom_complet(
                    get_value(dirigeant, "prenoms"), get_value(dirigeant, "nom")
                ),
                date_naissance=get_value(dirigeant, "date_naissance"),
                nationalite=get_value(dirigeant, "nationalite"),
                adresse=get_value(dirigeant, "adresse"),
                code_postal=get_value(dirigeant, "code_postal"),
                ville=get_value(dirigeant, "ville"),
                type_personne=get_value(dirigeant, "type_personne"),
                ordreaffichage=get_value(dirigeant, "ordreaffichage"),
                numerochrono=get_value(dirigeant, "numerochrono"),
                actif=get_value(dirigeant, "actif"),
                fonction=get_value(dirigeant, "fonction"),
            )

            dirigeants_formatted.append(dirigeant)

    return dirigeants_formatted
