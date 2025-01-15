from app.models.unite_legale import Dirigeant
from app.utils.helpers import get_value


def format_dirigeants(dirigeants=None):

    dirigeants_formatted = []

    if dirigeants:
        for dirigeant_data in dirigeants:

            dirigeant = dirigeant_data

            # We only send active dirigeant
            if dirigeant["actif"] == False:
                break

            dirigeant = Dirigeant(
                nom=get_value(dirigeant, "nom"),
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
