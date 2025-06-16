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
        {"name": "etat_rid", "type": "string", "facet": True, "optional": True, "sort": True},
        {"name": "date_creation", "type": "string", "optional": True, "index": False},
        {"name": "date_radiation", "type": "string", "optional": True, "index": False},
        {"name": "telephone", "type": "string", "optional": True, "index": False},
        {"name": "email", "type": "string", "optional": True, "index": False},
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
            "name": "dirigeants.prenoms",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "dirigeants.nom_personne_morale",
            "type": "string[]",
            "facet": True,
            "optionnal": True,
        },
        {
            "name": "dirigeants.date_naissance",
            "type": "string[]",
            "optionnal": True,
            "index": False,
        },
        {
            "name": "dirigeants.nationalite",
            "type": "string[]",
            "optionnal": True,
            "index": False,
        },
        {
            "name": "dirigeants.code_postal",
            "type": "string[]",
            "optionnal": True,
            "index": False,
        },
        {
            "name": "dirigeants.ville",
            "type": "string[]",
            "optionnal": True,
            "index": False,
        },
        {
            "name": "dirigeants.type_personne",
            "type": "string[]",
            "optionnal": True,
            "index": False,
        },
        {
            "name": "dirigeants.ordreaffichage",
            "type": "int32[]",
            "optionnal": True,
            "index": False,
        },
        {
            "name": "dirigeants.numerochrono",
            "type": "int32[]",
            "optionnal": True,
            "index": False,
        },
        {
            "name": "dirigeants.actif",
            "type": "bool[]",
            "optionnal": True,
            "index": False,
        },
        {
            "name": "dirigeants.fonction",
            "type": "string[]",
            "optionnal": True,
            "index": False,
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
