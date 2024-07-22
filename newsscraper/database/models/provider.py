from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..base_class import Base


class Providers(Base):
    pro_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    articles = relationship("Articles", back_populates="provider")
