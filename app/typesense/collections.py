# Collection is the name in typesense related to indexed schema
from app.typesense.connection import typesense_client
from loguru import logger
from typesense.exceptions import ObjectNotFound

entreprise_schema = {
    "name": "entreprises",
    "enable_nested_fields": True,
    "fields": [
        {"name": "rid", "type": "string", "facet": True},
        {"name": "designation", "type": "string", "facet": True, "optional": True},
        {"name": "sigle", "type": "string", "facet": True, "optional": True},
        {"name": "forme_juridique", "type": "string", "facet": True, "optional": True},
        {"name": "code_postal_postale", "type": "string", "optional": True},
        {"name": "ville_physique", "type": "string", "facet": True, "optional": True},
        {"name": "ape", "type": "string", "facet": True, "optional": True},
        {"name": "etat_rid", "type": "string", "optional": True},
        {"name": "date_creation", "type": "string", "facet": True, "optional": True},
        {"name": "date_radiation", "type": "string", "facet": True, "optional": True},
        {"name": "telephone", "type": "string", "optional": True},
        {"name": "email", "type": "string", "optional": True},
        {"name": "activites_secondaires", "type": "string", "optional": True},
        {"name": "adresse_physique", "type": "string", "facet": True, "optional": True},
        {"name": "adresse_postale", "type": "string", "optional": True},
        {"name": "code_ape", "type": "string", "facet": True, "optional": True},
        {"name": "etablissements", "type": "object[]", "optional": True},
        {
            "name": "etablissements.rid",
            "type": "string[]",
            "facet": True,
            "optional": True,
        },
        {
            "name": "etablissements.et",
            "type": "string[]",
            "facet": True,
            "optional": True,
        },
        {
            "name": "etablissements.enseigne",
            "type": "string[]",
            "facet": True,
            "optional": True,
        },
        {
            "name": "etablissements.ville_postale",
            "type": "string[]",
            "facet": True,
            "optional": True,
        },
        {
            "name": "etablissements.ville_physique",
            "type": "string[]",
            "facet": True,
            "optional": True,
        },
        {"name": "etablissements.situation", "type": "string[]", "optional": True},
        {
            "name": "etablissements.code_ape",
            "type": "string[]",
            "facet": True,
            "optional": True,
        },
        {
            "name": "etablissements.ape",
            "type": "string[]",
            "facet": True,
            "optional": True,
        },
        {
            "name": "etablissements.activites_secondaires",
            "type": "string[]",
            "optional": True,
        },
        {
            "name": "etablissements.adresse_physique",
            "type": "string[]",
            "facet": True,
            "optional": True,
        },
        {
            "name": "etablissements.adresse_postale",
            "type": "string[]",
            "facet": True,
            "optional": True,
        },
        {"name": "dirigeants", "type": "object[]", "optionnal": True},
        {
            "name": "dirigeants.nom",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "dirigeants.date_naissance",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "dirigeants.nationalite",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "dirigeants.code_postal",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "dirigeants.ville",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "dirigeants.type_personne",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "dirigeants.ordreaffichage",
            "type": "int32[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "dirigeants.numerochrono",
            "type": "int32[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "dirigeants.actif",
            "type": "bool[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "dirigeants.fonction",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
        {"name": "indicateurs_financiers", "type": "object[]", "optionnal": True},
        {
            "name": "indicateurs_financiers.noncommandable",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "indicateurs_financiers.diffusable",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
        # {"name": "indicateurs_financiers.resultat", "type": "float[]", "facet": True},
        # {"name": "indicateurs_financiers.devise", "type": "string[]", "facet": True},
        # {"name": "indicateurs_financiers.effectif", "type": "string[]", "facet": True},
        # {"name": "indicateurs_financiers.chiffredaffaire", "type": "string[]", "facet": True},
        {
            "name": "indicateurs_financiers.numerodepot",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "indicateurs_financiers.dureeexercice",
            "type": "int32[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "indicateurs_financiers.datedepot",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "indicateurs_financiers.datecloture",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
    ],
}


def create_schema_collection_and_documents():
    try:
        entreprise_collection = typesense_client.collections["entreprises"].retrieve()

        if entreprise_collection is not None:
            typesense_client.collections["entreprises"].delete()

        typesense_client.collections.create(entreprise_schema)
    except ObjectNotFound:
        logger.warning("première initialisation => creation de la collection")
        typesense_client.collections.create(entreprise_schema)
    except Exception as e:
        logger.exception(
            "An error occurred during the creation of collections for typesense:"
        )
        raise e
