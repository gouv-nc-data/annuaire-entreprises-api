from pydantic import BaseModel


class EntrepriseResponse(BaseModel):
    nom_complet: str | None = None
    ridet: str | None = None
    designation: str | None = None
    enseigne: str | None = None
    forme_juridique: str | None = None
    adresse_physique: str | None = None
    code_postal_physique: str | None = None
    ville_physique: str | None = None
    adresse_postale: str | None = None
    code_postal_postale: str | None = None
    ville_postale: str | None = None
    adresse_complete: str | None = None
    telephone: str | None = None
    email: str | None = None
    ape: str | None = None
    code_ape: str | None = None
    activites_secondaires: str | None = None
    code_nafa: str | None = None
    code_nafa_secondaires: str | None = None
    nb_salaries: int | None = None
    tranche_effectif_salaries: str | None = None
    taille_structure: str | None = None
    date_creation: str | None = None
    date_radiation: str | None = None
    motif_radiation: str | None = None
    convention_collective: str | None = None

    # Immatriculation RCS
    numero_rcs: str | None = None
    date_immat_rcs: str | None = None
    date_radiation_rsc: str | None = None
    capital_social: int | None = None
    capital_fixe: bool | None = None
    data_cloture_exercice_comptable: str | None = None
    duree_personne_morale: str | None = None

    # Immatriculation au répertoire des métiers (RM)
    numero_rm: str | None = None
    date_immat_rm: str | None = None
    date_radiation_rm: str | None = None

    # Immatriculation au registre de l'agriculture et pêche (RAP)
    numero_rap: str | None = None
    date_immat_rap: str | None = None
    date_radiation_rap: str | None = None

    # etablissements: Mapped[List["Etablissement"]] = relationship(
    #     back_populates="entreprise", cascade="all, delete-orphan"
    # )

    # dirigeants: Mapped[List["Dirigeant"]] = relationship(
    #     back_populates="entreprise", cascade="all, delete-orphan"
    # )

    # indicateurs_financiers: Mapped[List["IndicateursFinanciers"]] = relationship(
    #     back_populates="entreprise", cascade="all, delete-orphan"
    # )
