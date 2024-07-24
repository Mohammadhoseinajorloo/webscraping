from newsscraper.db.base_class import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Provider(Base):
    pro_id = Column(Integer, primary_key=True, index=True)
    pro_name = Column(String, index=True)
    article = relationship("Article", back_populates="provider")
