from webscraping.newsscraper.db.models.engin import get_engin
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=get_engin())


def get_session():
    return Session()
