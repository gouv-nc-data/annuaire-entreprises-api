from app.models.unite_legale import Etablissement
from app.utils.helpers import get_value
from app.services.formatters.rid import format_ridet
from app.services.formatters.nom_complet import format_nom_complet
from app.services.formatters.adresse_complete import format_adresse_complete


def format_etablissements(etablissements=None):

    etablissements_formatted = []

    if etablissements:
        for etablissement_data in etablissements:

            if isinstance(etablissement_data, dict):
                etablissement = etablissement_data
            else:
                etablissement = etablissement_data.__dict__

            etablissement = Etablissement(
                nom_complet=format_nom_complet(
                    get_value(etablissement, "enseigne"),
                    get_value(etablissement, "designation"),
                ),
                adresse_complete=format_adresse_complete(
                    get_value(etablissement, "adresse_physique"),
                    get_value(etablissement, "ville_physique"),
                    get_value(etablissement, "code_postal_physique"),
                ),
                type_etablissement=get_value(etablissement, "type_etablissement"),
                situation=get_value(etablissement, "situation"),
                rid=get_value(etablissement, "rid"),
                et=get_value(etablissement, "et"),
                ridet=format_ridet(
                    get_value(etablissement, "rid"), get_value(etablissement, "et")
                ),
                designation=get_value(etablissement, "designation"),
                enseigne=get_value(etablissement, "enseigne"),
                ape=get_value(etablissement, "ape"),
                code_ape=get_value(etablissement, "code_ape"),
                activites_secondaires=get_value(etablissement, "activites_secondaires"),
                code_nafa=get_value(etablissement, "code_nafa"),
                code_nafa_secondaires=get_value(etablissement, "code_nafa_secondaires"),
                adresse_physique=get_value(etablissement, "adresse_physique"),
                code_postal_physique=get_value(etablissement, "code_postal_physique"),
                ville_physique=get_value(etablissement, "ville_physique"),
                adresse_postale=get_value(etablissement, "adresse_postale"),
                code_postal_postale=get_value(etablissement, "code_postal_postale"),
                ville_postale=get_value(etablissement, "ville_postale"),
                date_creation=get_value(etablissement, "date_creation"),
                date_debut_activite=get_value(etablissement, "date_debut_activite"),
                convention_collective=get_value(etablissement, "convention_collective"),
            )

            etablissements_formatted.append(etablissement)

    return etablissements_formatted
