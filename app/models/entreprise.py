from pydantic import BaseModel


class EntrepriseResponse(BaseModel):
    nom_complet: str | None = None
    ridet: str | None = None
    sigle: str | None = None
    enseigne: str | None = None
    forme_juridique: str | None = None
    adresse_complete: str | None = None
    adresse: str | None = None
    code_postal: str | None = None
    ville: str | None = None
