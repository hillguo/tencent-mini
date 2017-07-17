from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, text, Float, DateTime, ForeignKey

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(20))
    user_avatar = Column(String(100))

class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True)
    content = Column(String(140))
    story_id = Column(Integer, ForeignKey('story.story_id'))
    up = Column(Integer)
    created_at = Column(DateTime)

class Story(Base):
    __tablename__ = 'story'
    story_id = Column(Integer, primary_key=True)
    content = Column(String(140))
    song_id = Column(Integer, ForeignKey('song.song_id'))
    up = Column(Integer)
    user_id = Column(String, ForeignKey('user.user_id'))
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(DateTime)

class Song(Base):
    __tablename__ = 'song'
    song_id = Column(Integer, primary_key=True)
    song_link = Column(String(100))
    lrc_link = Column(String(100))
    song_pic_small = Column(String(100))
    song_name = Column(String(100))
    tag = Column(String(100))

class LikeStory(Base):
    __tablename__ = 'likestory'
    like_id = Column(Integer, primary_key=True)
    user_id = Column(String(50), ForeignKey('user.user_id'))
    story_id = Column(Integer, ForeignKey('story.story_id'))



