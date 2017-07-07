import tornado.web

from sqlalchemy import create_engine
from sqlalchemy import Column,text, Integer, String, DateTime, Boolean
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

class IndexHandler(BaseHandler):
    def get(self):
        sql=text("show tables")
        res=self.db.execute(sql).fetchall()
        print(res)
        self.write("hello")