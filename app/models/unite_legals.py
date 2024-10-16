from typing import Literal
from pydantic import BaseModel


class Etablissement(BaseModel):
    name: str | None = None
    activite_principale: str | None = None
    adresse: str | None = None
    date_creation: str | None = None


class UniteLegaleResponse(BaseModel):
    ridet: str
    nom_complet: str | None = None
    date_creation: str | None = None
    siege: Etablissement = None
    etablissements: list[Etablissement] | None = None
