from ..base_class import Base
from sqlalchemy import Column, Integer, String, Text, Time, create_engine, ForeignKey
from sqlalchemy.orm import relationship
from ..base_class import Base


class Articles(Base):
    art_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    image = Column(String, nullable=True)
    title = Column(String, nullable=False)
    date = Column(Time, nullable=False)
    link = Column(Text, nullable=False)
    pro_id = Column(Integer, ForeignKey("providers.pro_id"))
    outhor = Column(String, nullable=True)
    summary = Column(Text, nullable=True)
    provider = relationship("Providers", back_populates="articles")
