from sqlalchemy import Column, Integer, String
from app.database.connection import Base

from sqlalchemy import Date, Boolean, ForeignKey
from typing import List
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy.orm import Mapped


class Entreprise(Base):
    __tablename__ = "entreprise"

    id = Column(Integer, primary_key=True)
    etat_inscription = Column(String)
    rid = Column(String, unique=True)
    etat_rid = Column(String)  # I=Inscrit R=Radié S=sommeil
    designation = Column(String)
    sigle = Column(String)
    forme_juridique = Column(String)
    adresse_physique = Column(String)
    code_postal_physique = Column(String)
    ville_physique = Column(String)
    adresse_postale = Column(String)
    code_postal_postale = Column(String)
    ville_postale = Column(String)
    telephone = Column(String)
    email = Column(String)
    ape = Column(String)
    code_ape = Column(String)
    activites_secondaires = Column(String)
    code_nafa = Column(String)
    code_nafa_secondaires = Column(String)
    nb_salaries = Column(Integer)
    tranche_effectif_salaries = Column(String)
    taille_structure = Column(String)
    date_creation = Column(Date)
    date_radiation = Column(Date)
    motif_radiation = Column(String)
    convention_collective = Column(String)
    situation_entreprise = Column(String)
    

    # Immatriculation RCS
    numero_rcs = Column(String)
    date_immat_rcs = Column(Date)
    date_radiation_rsc = Column(Date)
    capital_social = Column(Integer)
    capital_fixe = Column(Boolean)
    data_cloture_exercice_comptable = Column(String)
    duree_personne_morale = Column(String)

    # Immatriculation au répertoire des métiers (RM)
    numero_rm = Column(String)
    date_immat_rm = Column(Date)
    date_radiation_rm = Column(Date)

    # Immatriculation au registre de l'agriculture et pêche (RAP)
    numero_rap = Column(String)
    date_immat_rap = Column(Date)
    date_radiation_rap = Column(Date)

    etablissements: Mapped[List["Etablissement"]] = relationship(
        back_populates="entreprise", cascade="all, delete-orphan"
    )

    dirigeants: Mapped[List["Dirigeant"]] = relationship(
        back_populates="entreprise", cascade="all, delete-orphan"
    )

    # indicateurs_financiers: Mapped[List["IndicateursFinanciers"]] = relationship(
    #     back_populates="entreprise", cascade="all, delete-orphan"
    # )


class Etablissement(Base):
    __tablename__ = "etablissement"

    id = Column(Integer, primary_key=True)
    type_etablissement = Column(String)
    situation = Column(String)
    rid = Column(String)
    et = Column(String)
    designation = Column(String)
    enseigne = Column(String)
    ape = Column(String)
    code_ape = Column(String)
    activites_secondaires = Column(String)
    code_nafa = Column(String)
    code_nafa_secondaires = Column(String)
    adresse_physique = Column(String)
    code_postal_physique = Column(String)
    ville_physique = Column(String)
    adresse_postale = Column(String)
    code_postal_postale = Column(String)
    ville_postale = Column(String)
    date_creation = Column(Date)
    date_debut_activite = Column(Date)
    date_fin_activite = Column(Date)
    convention_collective = Column(String)

    entreprise_id: Mapped[int] = mapped_column(ForeignKey("entreprise.id"))

    entreprise: Mapped["Entreprise"] = relationship(back_populates="etablissements")

    dirigeants: Mapped[List["Dirigeant"]] = relationship(
        back_populates="etablissement", cascade="all, delete-orphan"
    )

    # indicateurs_financiers: Mapped[List["IndicateursFinanciers"]] = relationship(
    #     back_populates="etablissement", cascade="all, delete-orphan"
    # )


class Dirigeant(Base):
    __tablename__ = "dirigeant"

    id = Column(Integer, primary_key=True)
    role = Column(String)
    nom = Column(String)
    date_naissance = Column(String)
    nationalite = Column(String)
    adresse = Column(String)
    code_postal = Column(String)
    ville = Column(String)
    titre_cma = Column(String)
    date_de_fonction_rm = Column(Date)
    date_de_fonction_ra = Column(Date)
    situation_matrimoniale = Column(String)
    maitre_apprentissage = Column(String)
    qualifie_dans_son_metier = Column(String)

    entreprise_id: Mapped[int] = mapped_column(ForeignKey("entreprise.id"), nullable=True)

    entreprise: Mapped["Entreprise"] = relationship(back_populates="dirigeants")

    etablissement_id: Mapped[int] = mapped_column(ForeignKey("etablissement.id"), nullable=True)

    etablissement: Mapped["Etablissement"] = relationship(
        back_populates="dirigeants"
    )


class IndicateursFinanciers(Base):
    __tablename__ = "indicateurs_financiers"

    id = Column(Integer, primary_key=True)
    date_cloture = Column(Date)
    chiffre_affaire = Column(Integer)
    marge_brute = Column(Integer)
    excedent_brut_exploitation = Column(Integer)
    resultat_net = Column(Integer)

    entreprise_id: Mapped[int] = mapped_column(ForeignKey("entreprise.id"), nullable=True)

#     entreprise: Mapped["Entreprise"] = relationship(back_populates="dirigeants")

    etablissement_id: Mapped[int] = mapped_column(ForeignKey("etablissement.id"), nullable=True)

#     etablissement: Mapped["Etablissement"] = relationship(
#         back_populates="indicateurs_financiers"
#     )


class Bilan(Base):
    __tablename__ = "bilan"

    id = Column(Integer, primary_key=True)
    comptes_annuels = Column(String)
    actes = Column(String)
    entreprise_id: Mapped[int] = mapped_column(
        ForeignKey("entreprise.id"), nullable=True
    )
    etablissement_id: Mapped[int] = mapped_column(
        ForeignKey("etablissement.id"), nullable=True
    )
