from app.models.unite_legale import IndicateursFinanciers
from app.services.formatters.date import format_date
from app.utils.helpers import get_value


def format_indicateurs_financiers(indicateurs_financiers=None):

    indicateurs_financiers_formatted = []

    if indicateurs_financiers:
        for indicateur_financier_data in indicateurs_financiers:

            if isinstance(indicateur_financier_data, dict):
                indicateur_financier = indicateur_financier_data
            else:
                indicateur_financier = indicateur_financier_data.__dict__

            # We only send active diffusable data
            if indicateur_financier["diffusable"] == "false":
                break

            indicateur_financier = IndicateursFinanciers(
                noncommandable=get_value(indicateur_financier, "noncommandable"),
                diffusable=get_value(indicateur_financier, "diffusable"),
                numerodepot=get_value(indicateur_financier, "numerodepot"),
                dureeexercice=get_value(indicateur_financier, "dureeexercice"),
                datedepot=format_date(get_value(indicateur_financier, "datedepot")),
                datecloture=format_date(get_value(indicateur_financier, "datecloture")),
            )

            indicateurs_financiers_formatted.append(indicateur_financier)

    return indicateurs_financiers_formatted
