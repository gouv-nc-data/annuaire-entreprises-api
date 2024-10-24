from dotenv import dotenv_values
from pydantic import ConfigDict

import os

## Surcharge de l'ordre de définition des variables. Celle de l'OS sont prises en compte en premier. Sinon, si le fichier n'existe pas, il n'y a pas de valeur, ce qui est le cas dans le container
config = {
    **os.environ,
    **dotenv_values(
        ".env",
    ),
}


class SqlAlchemyConfig(ConfigDict):
    database_url: str = config["DATABASE_URL"] or "localhost"
    database_username: str = config["DATABASE_USERNAME"] or "postgres"
    database_password: str = config["DATABASE_PASSWORD"] or "password"
    database_name: str = config["DATABASE_NAME"] or "postgres"


class SentryConfig(ConfigDict):
    dsn: str = config["SENTRY_DSN"]


class Settings(ConfigDict):
    sql_alchemy = SqlAlchemyConfig
    sentry = SentryConfig
    env: str = config["ENV"] or "development"
