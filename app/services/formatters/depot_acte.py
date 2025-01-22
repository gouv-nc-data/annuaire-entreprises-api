from app.models.unite_legale import DepotActe
from app.services.formatters.date import format_date
from app.utils.helpers import get_value


def format_depot_acte(depot_acte=None):

    depot_acte_formatted = []

    if depot_acte:
        for depot_acte_data in depot_acte:

            if isinstance(depot_acte_data, dict):
                depot_acte = depot_acte_data
            else:
                depot_acte = depot_acte_data.__dict__

            # We only send diffusable data
            if depot_acte["diffusable"] == "false":
                break

            depot_acte = DepotActe(
                diffusable=get_value(depot_acte, "diffusable"),
                numerodepot=get_value(depot_acte, "numerodepot"),
                datedepot=format_date(get_value(depot_acte, "datedepot")),
                date=format_date(depot_acte["_date"]),
                noncommandable=get_value(depot_acte, "noncommandable"),
                type=get_value(depot_acte, "_type"),
                ordreaffichage=get_value(depot_acte, "ordreaffichage"),
                numerochrono=get_value(depot_acte, "numerochrono"),
                rid=get_value(depot_acte, "rid"),
                libelle=get_value(depot_acte, "libelle"),
                nature=get_value(depot_acte, "nature"),
            )

            print("depot acte after ????", depot_acte)

            depot_acte_formatted.append(depot_acte)

    return depot_acte_formatted
