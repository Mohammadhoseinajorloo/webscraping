from datetime import datetime

from newsscraper.db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship


class Article(Base):
    art_id = Column(Integer, primary_key=True)
    title = Column(String , nullable=False)
    summary = Column(Text, nullable=True)
    pro_id = Column(Integer, ForeignKey("provider.pro_id"))
    provider = relationship("Provider", back_populates="article")
    date = Column(DateTime, nullable=False)
    link = Column(String, nullable=False)
    author = Column(String, nullable=True)
    image = Column(String, nullable=True)
