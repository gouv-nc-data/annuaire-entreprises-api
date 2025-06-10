from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


from app.config import settings

sql_alchemy_settings = settings.sql_alchemy

url = URL.create(
    drivername="postgresql",
    username=sql_alchemy_settings.database_username,
    password=sql_alchemy_settings.database_password,
    host=sql_alchemy_settings.database_url,
    database=sql_alchemy_settings.database_name,
    query=dict(application_name="api")
)

engine = create_engine(url).execution_options(isolation_level="AUTOCOMMIT")

SessionMaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)
LocalSession = scoped_session(SessionMaker)

Base = declarative_base()
