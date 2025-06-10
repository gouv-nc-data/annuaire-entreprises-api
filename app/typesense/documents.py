from sqlalchemy.orm import joinedload
from sqlalchemy.exc import PendingRollbackError
from app.database import models
from app.database.connection import LocalSession

from app.typesense.connection import typesense_client
from fastapi import Depends
from sqlalchemy.orm import Session
from loguru import logger

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        LocalSession.remove()

# Documents is the name in typesense related to indexed objects (item)
def create_typesense_nested_documents(db: Session = Depends(get_db)):
    
    Entreprise = models.Entreprise

    try:
        entreprises = (
            db.query(Entreprise)
            .options(
                joinedload(Entreprise.etablissements), joinedload(Entreprise.dirigeants)
            )
            .all()
        )

        documents = []

        for entreprise in entreprises:
            # Convert each entreprise and its etablissements, dirigeants to a dictionary

            entreprise_data = {
                "rid": entreprise.rid,
                "designation": entreprise.designation,
                "sigle": entreprise.sigle,
                "forme_juridique": entreprise.forme_juridique,
                "code_postal_postale": entreprise.code_postal_postale,
                "ville_physique": entreprise.ville_physique,
                "ape": entreprise.ape,
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
                "dirigeants": [
                    {
                        "nom": dirigeant.nom or "null",
                        "prenoms": dirigeant.prenoms or "null",
                        "nom_personne_morale": dirigeant.nom_personne_morale or "null",
                        "date_naissance": dirigeant.date_naissance,
                        "nationalite": dirigeant.nationalite,
                        "adresse": dirigeant.adresse,
                        "code_postal": dirigeant.code_postal,
                        "ville": dirigeant.ville,
                        "type_personne": dirigeant.type_personne,
                        "ordreaffichage": dirigeant.ordreaffichage,
                        "numerochrono": dirigeant.numerochrono,
                        "actif": dirigeant.actif,
                        "fonction": dirigeant.fonction,
                    }
                    for dirigeant in entreprise.dirigeants
                ],
            }

            # Typense can't index the object if one of its nested field is empty
            # This trick is used to correclty index the parent entreprise even if the nested field (dirigeants) is empty
            # This is how typesense works, might change in the future...
            # We're creating false values for 1 nested field
            # Those data are not sent the API Result tho
            # This is only used to index the parent
            if len(entreprise_data["dirigeants"]) == 0:
                entreprise_data["dirigeants"] = [
                    {
                        "nom": "null",
                        "prenoms": "null",
                        "nom_personne_morale": "null",
                        "actif": False,
                        "date_naissance": "null",
                        "nationalite": "null",
                        # "adresse": "null",
                        "code_postal": "null",
                        "ville": "null",
                        "type_personne": "null",
                        "ordreaffichage": 0,
                        "numerochrono": 0,
                        "fonction": "null",
                    }
                ]

            # Write the dictionary as a JSON object to the file
            documents.append(entreprise_data)

        typesense_client.collections["entreprises"].documents.import_(
            documents, {"action": "create", "dirty_values": "coerce_or_drop"}
        )

    except Exception as e:
        logger.exception(
            "An error occurred during the creation of the documents for typesense"
        )
        raise e
