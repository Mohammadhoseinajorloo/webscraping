from ..base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Provider(Base):
    __tablename__ = "providers"
    pro_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    articles = relationship("Article", back_populates="provider")