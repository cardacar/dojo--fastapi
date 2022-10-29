from importlib.metadata import metadata
from sqlalchemy import create_engine, MetaData
from .settings import Settings

settings = Settings()
engine = create_engine(settings.url_database)
metadata = MetaData()

conn = engine.connect()