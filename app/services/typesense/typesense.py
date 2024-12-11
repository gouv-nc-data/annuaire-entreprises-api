import typesense
import json

from sqlalchemy.orm import joinedload

from app.database import models
from app.database.connection import SessionLocal


db = SessionLocal()

client = typesense.Client(
    {
        "nodes": [
            {
                "host": "localhost",  # For Typesense Cloud use xxx.a1.typesense.net
                "port": "8108",  # For Typesense Cloud use 443
                "protocol": "http",  # For Typesense Cloud use https
            }
        ],
        "api_key": "xyz",
        "connection_timeout_seconds": 2,
    }
)

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


def create_typesense_nested_documents():
    Entreprise = models.Entreprise

    try:
        entreprises = db.query(Entreprise).options(joinedload("*")).all()

        with open("entreprise_etablissements.jsonl", "w", encoding="utf-8") as file:
            for entreprise in entreprises:
                # Convert each entreprise and its etablissements to a dictionary

                entreprise_data = {
                    "rid": entreprise.rid,
                    "designation": entreprise.designation,
                    "sigle": entreprise.sigle,
                    "forme_juridique": entreprise.forme_juridique,
                    "code_postal_postale": entreprise.code_postal_postale,
                    "ville_physique": entreprise.ville_physique,
                    "ape": entreprise.ape,
                    "situation_entreprise": entreprise.situation_entreprise,
                    "etat_rid": entreprise.etat_rid,
                    "date_creation": str(entreprise.date_creation),
                    "date_radiation": str(entreprise.date_radiation),
                    "telephone": entreprise.telephone,
                    "email": entreprise.email,
                    "activites_secondaires": entreprise.activites_secondaires,
                    "adresse_physique": entreprise.adresse_physique,
                    "adresse_postale": entreprise.adresse_postale,
                    "code_ape": entreprise.code_ape,
                    "etablissements": [
                        {
                            "rid": etablissement.rid,
                            "et": etablissement.et,
                            "enseigne": etablissement.enseigne,
                            "ville_postale": etablissement.ville_postale,
                            "ville_physique": etablissement.ville_physique,
                            "situation": etablissement.situation,
                            "code_ape": etablissement.code_ape,
                            "ape": etablissement.ape,
                            "activites_secondaires": etablissement.activites_secondaires,
                            "adresse_physique": etablissement.adresse_physique,
                            "adresse_postale": etablissement.adresse_postale,
                            "ape": etablissement.ape,
                        }
                        for etablissement in entreprise.etablissements
                    ],
                }

                # Write the dictionary as a JSON object to the file
                file.write(json.dumps(entreprise_data, ensure_ascii=False) + "\n")

        print(f"Data successfully written to entreprise_etablissements.jsonl")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_schema_collection_and_documents():
    client.collections.create(entreprise_schema)
    create_typesense_nested_documents()
