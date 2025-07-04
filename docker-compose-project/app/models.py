from sqlalchemy import Column, Integer, String
from .database import Base

class Quote(Base):
    __tablename__ = "quotes"

    index = Column(Integer, primary_key=True, index=True, autoincrement=True)
    author = Column(String(255), index=True)
    text = Column(String(255), index=True)

