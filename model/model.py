
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, text

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    user_name = Column(String(20))
    user_avatar = Column(String(100))
    
