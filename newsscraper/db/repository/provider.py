from webscraping.newsscraper.db.models.provider import Provider
from sqlalchemy.orm import Session


def get_provider(name: str, session: Session):
    provider = session.query(Provider).filter_by(name=name).first()
    return provider


def add_provider(name: str, session: Session):
    provider = Provider(name)
    session.add(provider)
    session.commit()
