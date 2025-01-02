from sqlalchemy.orm import joinedload

from app.database import models
from app.database.connection import SessionLocal

from app.typesense.connection import typesense_client

from loguru import logger
db = SessionLocal()

# Documents is the name in typesense related to indexed objects (item)
def create_typesense_nested_documents():
    Entreprise = models.Entreprise

    try:
        entreprises = db.query(Entreprise).options(joinedload("*")).all()

        documents = []

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
                    }
                    for etablissement in entreprise.etablissements
                ],
            }

            # Write the dictionary as a JSON object to the file
            documents.append(entreprise_data)

        typesense_client.collections["entreprises"].documents.import_(
            documents, {"action": "create"}
        )

    except Exception as e:
        logger.exception("An error occurred during the creation of the documents for typesense")
        raise e
