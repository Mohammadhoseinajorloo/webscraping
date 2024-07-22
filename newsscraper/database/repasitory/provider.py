from sqlalchemy.orm import Session
from ..models.provider import Providers


def add_provider(provider: str, db: Session):
    provider = Providers(
        name=provider
    )
    db.add(provider)
    db.commit()
    db.refresh(provider)
    return provider
