from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

config = dotenv_values(".env")

SQLALCHEMY_DATABASE_URL = config["DATABASE_URL"]
SQLALCHEMY_DATABASE_USER = config["DATABASE_USERNAME"]
SQLALCHEMY_DATABASE_PASSWORD = config["DATABASE_PASSWORD"]
SQLALCHEMY_DATABASE_NAME = config["DATABASE_NAME"]

url = URL.create(
    drivername="postgresql",
    username=SQLALCHEMY_DATABASE_USER,
    password=SQLALCHEMY_DATABASE_PASSWORD,
    host=SQLALCHEMY_DATABASE_URL,
    database=SQLALCHEMY_DATABASE_NAME,
)

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
