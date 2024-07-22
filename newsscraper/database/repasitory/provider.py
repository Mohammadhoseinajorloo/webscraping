from sqlalchemy.orm import Session
from webscraping.newsscraper.database.models.provider import Providers


def add_provider(provider: str, db: Session):
    provider = Providers(
        name=provider
    )
    db.add(provider)
    db.commit()
    db.refresh(provider)
    return provider
