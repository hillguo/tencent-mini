import json
import os
import binascii
import tornado.web

import tornado.gen


class BaseHandler(tornado.web.RequestHandler):

    __TOKEN_LIST = {}

    @property
    def db(self):
        return self.application.db


    def generate_token(self):
        while True:
            new_token = binascii.hexlify(os.urandom(16)).decode("utf-8")
            if new_token not in self.__TOKEN_LIST:
                return new_token

    def set_token(self,token,userid):
        self.__TOKEN_LIST[token] = userid
        #self.set_secure_cookie('_token', token)
        

    def get_current_user(self):
        #token = self.get_secure_cookie("_token").decode()
        token = self.get_argument("token",None)
        if token and token in self.__TOKEN_LIST:
            userid = self.__TOKEN_LIST[token]
            return userid
        return None
    
    def valid_user(self):
        token = self.get_argument("token",None)
        user_id = self.get_argument("user_id",None)
        if token and user_id and token in self.__TOKEN_LIST:
            if user_id == self.__TOKEN_LIST[token]:
                return True
        return False
