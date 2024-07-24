from sqlalchemy import create_engine
from webscraping.newsscraper.core.config import settings
from webscraping.newsscraper.db.base_class import Base


def get_engin():
    return create_engine(settings.DATABASE_URL)


def create_table():
    engin = get_engin()
    Base.metadata.create_all(engin)


create_table()
