from webscraping.newsscraper.db.models.provider import Provider
from sqlalchemy.orm import Session


def get_provider(name: str, session: Session):
    provider = session.query(Provider).filter_by(name=name).first()
    return provider
