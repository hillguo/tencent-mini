import json

from sqlalchemy import Column,text, Integer, String, DateTime, Boolean
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound

from model.user_model import User
from handler.base_handler import BaseHandler          

class IndexHandler(BaseHandler):
    def get(self):
        sql=text("show tables")
        res=self.db.execute(sql).fetchall()
        self.write("hello")


class LoginHandler(BaseHandler):
    def post(self):
        user_id = self.get_argument("user_id",None)
        if user_id == None :
            self.write_miss_argument()
            return None 
        user=self.db.query(User).filter(User.user_qq_id==user_id).first()
        if user == None:
            user = User(user_qq_id=user_id)
            self.db.add(user)
            self.db.commit()
        new_token = self.generate_token()
        self.set_token(new_token,user_id)
        res ={}
        res["code"] = 0
        res["token"] = new_token
        res["msg"] = "login success !"
        self.write(res)
