from app.models.unite_legale import Dirigeant
from app.utils.helpers import get_value


def format_dirigeants(dirigeants=None):

    dirigeants_formatted = []

    if dirigeants:
        for dirigeant_data in dirigeants:

            dirigeant = dirigeant_data.__dict__

            dirigeant = Dirigeant(
                nom=get_value(dirigeant, "nom"),
                role=get_value(dirigeant, "role"),
                prenoms=get_value(dirigeant, "prenoms"),
                date_de_naissance=get_value(dirigeant, "date_de_naissance"),
                nationalite=get_value(dirigeant, "nationalite"),
            )

            dirigeants_formatted.append(dirigeant)

    return dirigeants_formatted
