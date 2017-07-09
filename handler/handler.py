import json
import os
import binascii

import tornado.web

from sqlalchemy import create_engine
from sqlalchemy import Column,text, Integer, String, DateTime, Boolean
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound



from model.model import User


class BaseHandler(tornado.web.RequestHandler):

    __TOKEN_LIST = {}

    @property
    def db(self):
        return self.application.db

    def write_miss_argument(self):
        res={}
        res["code"] = 1
        res["message"] = "Miss arguments"
        self.write(res)

    def generate_token(self):
        while True:
            new_token = binascii.hexlify(os.urandom(16)).decode("utf-8")
            if new_token not in self.__TOKEN_LIST:
                return new_token

    def set_token(self,token,userid):
        self.__TOKEN_LIST[token] = userid
        self.set_secure_cookie('_token', token)
        

    def get_current_user(self):
        token = self.get_secure_cookie("_token").decode()
        if token and token in self.__TOKEN_LIST:
            userid = self.__TOKEN_LIST[token]
            return userid
        return None

class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        sql=text("show tables")
        res=self.db.execute(sql).fetchall()
        self.write("hello")


class LoginHandler(BaseHandler):
    def get(self):
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
        self.write("ok")

class Sample(BaseHandler):
    '''例子：1. 所有处理类继承 BaseHandle
             2. get 处理get 请求 , post 方法 处理 post 请求
             3. self.get_argument("arg_name",None) 获取传来的参数，没有返回None
             4. 所有 有可能被 越权 的操作，都需要在 加@tornado.web.authenticated 验证登录
             5. 返回值均为json
             6. 例子： 根据请求的 user_id 返回个人信息. (紧作参考，不严禁)
    '''
    @tornado.web.authenticated
    def post(self):
        user_id = self.get_argument("user_id",None)
        if user_id != self.current_user:
            self.write("越权操作")
            return
        if user_id :
            user = self.db.query(User).filter(User.user_qq_id == user_id).first()
            res={}
            res["user_id"]=user.user_qq_id
            res["user_name"]=user.user_name
            res["user_pic"] = user.user_pic
            self.write(res)
        else :
            self.write("error")
        
