from typing import List

from app.database.connection import Base

from sqlalchemy import Column, String, Date, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Etablissement(Base):
    __tablename__ = "etablissement"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    adresse = Column(String)
    date_creation = Column(Date)
    unite_legale_id: Mapped[String] = mapped_column(ForeignKey("unite_legal.ridet"))


class UniteLegale(Base):
    __tablename__ = "unite_legal"

    ridet = Column(String, primary_key=True)
    nom_complet = Column(String)
    date_creation = Column(Date)
    etablissements: Mapped[List["Etablissement"]] = relationship()
