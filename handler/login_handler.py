import json
import traceback

from sqlalchemy import Column,text, Integer, String, DateTime, Boolean
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound
import tornado.gen
from model.model import User

from handler.base_handler import BaseHandler          




class IndexHandler(BaseHandler):
    def get(self):
        sql=text("show tables")
        res=self.db.execute(sql).fetchall()
        self.write("hello")


class LoginHandler(BaseHandler):
    def post(self):
        user_id = self.get_argument("user_id",None)
        user_name = self.get_argument("user_name",None)
        user_avatar = self.get_argument("user_avatar",None)
        if user_id == None :
            res ={}
            res["code"] = -1
            res["errinfo"] = "参数错误"
            self.write(res)
            return None 
        try:
            user=self.db.query(User).filter(User.user_id==user_id).first()
            if user == None:
                user = User(user_id=user_id,user_name=user_name,user_avatar=user_avatar)
                self.db.add(user)
                self.db.commit()
        except BaseException as e:
            msg = traceback.format_exc()
            print(msg)
            res={}
            res["code"]= -1
            res["errinfo"]= "参数错误"
            self.write(res)
            return None
        new_token = self.generate_token()
        self.set_token(new_token,user_id)
        res ={}
        res["code"] = 0
        data ={}
        data["token"]=new_token
        res["data"] = data
        res["errinfo"] = "login success !"
        self.write(res)

class UserInfoHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        val = yield self.valid_user()
        if not val:
            res={}
            res["code"] = -1
            res["errinfo"] = "不合法用户"
            self.write(res)
            return None
        user_id = self.get_argument("user_id",None)
        user = self.db.query(User).filter(User.user_id==user_id).first()
        data={}
        data["user_id"]=user.user_id
        data["user_name"]=user.user_name
        data["user_avatar"]=user.user_avatar
        res ={}
        res["code"]=0
        res["data"]=data
        res["errinfo"]="success!"
        self.write(res)


class LikeSongHandler(BaseHandler):
    def get(self):
        rep = {"code" :0, "errinfo":"success"}
        try:
            user_id = self.get_argument("user_id")
            song_id = self.get_argument("song_id")
        except Exception as e:
            rep["code"] = -1;
            rep["errinfo"] = "参数有问题"
            self.write(rep)
            return

        try:

            sql = text("select * from historysong where user_id='" + user_id + "' and song_id=" + song_id)
            res = self.db.execute(sql).first()
            print(res)
            if not res:
                sql =text("insert into historysong  (user_id,song_id) values ('"+user_id+"',"+song_id+" )" )
                res = self.db.execute(sql)
                self.db.commit()
            # if not res:
            # ls =LikeSong(user_id=user_id,song_id=song_id)
            # self.db.add(ls)
            #self.db.commit()
        except Exception as e:
            print(e)
            rep["code"] = -2;
            rep["errinfo"] = "数据库插入失败"
            self.write(rep)
            return

        self.write(rep)


class HistorySongHandler(BaseHandler):
    def get(self):
        res={"code":0,"data":" ","errinfo":"success"}
        user_id=self.get_argument("user_id",None)

        if user_id ==None:
            res["code"]=-1
            res["errinfo"]="invalid args"
            self.write(res)
            return
        sql=text("select song_id from historysong where user_id='"+user_id+"'")
        datas=self.db.execute(sql).fetchall()
        l=[]
        for data in datas:
            l.append(data[0])
        print(l)
        res["data"]=l
        self.write(res)

