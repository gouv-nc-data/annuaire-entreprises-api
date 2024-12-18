from dotenv import dotenv_values
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings
from pathlib import Path
import os
from functools import lru_cache

## Surcharge de l'ordre de définition des variables. Celle de l'OS sont prises en compte en premier. Sinon, si le fichier n'existe pas, il n'y a pas de valeur, ce qui est le cas dans le container
config = {
    **os.environ,
    **dotenv_values(
        ".env",
    ),
}


class SqlAlchemyConfig(BaseSettings):
    database_url: str = Field(config["DATABASE_URL"] or "localhost")
    database_username: str = Field(config["DATABASE_USERNAME"] or "postgres")
    database_password: str = Field(config["DATABASE_PASSWORD"] or "password")
    database_name: str = Field(config["DATABASE_NAME"] or "postgres")


class DocsConfig(BaseSettings):
    doc_path: Path = Field(
        default_factory=lambda: Path(__file__).parent / "doc" / "open-api.yml"
    )

    @field_validator("doc_path")
    def validate_path(cls, v):
        if not v.exists():
            raise ValueError(f"The specified path does not exist: {v}")
        return v


# class SentryConfig(ConfigDict):
#     dsn: str = config["SENTRY_DSN"]


class TypesenseConfig(BaseSettings):
    typesense_api_key: str = Field(config["TYPESENSE_API_KEY"])
    typesense_api_host: str = Field(config["TYPESENSE_API_HOST"])
    typesense_api_port: str = Field(config["TYPESENSE_API_PORT"])


class Settings(BaseSettings):
    sql_alchemy: SqlAlchemyConfig = Field(default_factory=SqlAlchemyConfig)
    typesense: TypesenseConfig = Field(default_factory=TypesenseConfig)
    openapi: DocsConfig = Field(default_factory=DocsConfig)
    # sentry = SentryConfig
    env: str = "development"  # config["ENV"] or "development"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
