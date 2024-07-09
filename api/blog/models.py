from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String(100), nullable=False)
    user_phone = Column(Integer, nullable=False)
    user_lastname = Column(String, nullable=False)

class Photo(Base):
    __tablename__ = 'photo'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
