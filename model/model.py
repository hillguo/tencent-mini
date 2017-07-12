# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    user_id = Column(String(50), primary_key=True)
    user_name = Column(String(50))
    user_avatar = Column(String(200))
