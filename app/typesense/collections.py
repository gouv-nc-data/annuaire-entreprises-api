# Collection is the name in typesense related to indexed schema
import logging
from app.typesense.connection import typesense_client


log = logging.getLogger(__name__)
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
        {"name": "situation_entreprise", "type": "string", "optional": True},
        {"name": "etat_rid", "type": "string", "optional": True},
        {"name": "date_creation", "type": "string", "facet": True, "optional": True},
        {"name": "date_radiation", "type": "string", "facet": True, "optional": True},
        {"name": "telephone", "type": "string", "optional": True},
        {"name": "email", "type": "string", "optional": True},
        {"name": "activites_secondaires", "type": "string", "optional": True},
        {"name": "adresse_physique", "type": "string", "facet": True, "optional": True},
        {"name": "adresse_postale", "type": "string", "optional": True},
        {"name": "code_ape", "type": "string", "facet": True, "optional": True},
        {"name": "etablissements", "type": "object[]"},
        {"name": "etablissements.rid", "type": "string[]", "facet": True},
        {"name": "etablissements.et", "type": "string[]", "facet": True},
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
    ],
}


def create_schema_collection_and_documents():
    try:
        entreprise_collection = typesense_client.collections["entreprises"].retrieve()

        if entreprise_collection is not None:
            typesense_client.collections["entreprises"].delete()

        typesense_client.collections.create(entreprise_schema)

    except Exception as e:
        log.error("An error occurred during the creation of collections for typesense:", e)
        raise e
