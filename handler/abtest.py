import json
import traceback

import tornado.httpclient
import tornado.gen
from tornado.concurrent import run_on_executor


from handler.base_handler import BaseHandler          
from concurrent.futures import ThreadPoolExecutor


class ABTest1(BaseHandler):
    
    def get(self,user_id):
        res={"code":0,"data":"","errinfo":"success"}
        if user_id == None:
            res["code"] = -1
            res["errinfo"] = "invalid args"

        client = tornado.httpclient.HTTPClient()
        data = client.fetch("http://118.89.60.80:8000/recommend/"+user_id)
        if data.code == 200:
            print(data.body)
            res["data"]=data.body.decode()
        else:
            res["code"]=-1
            res["errinfo"]="data error"
        self.write(res)
        self.finish()
        client.close()
           
class ABTest2(BaseHandler):
    
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self,user_id):
        res={"code":0,"data":"","errinfo":"success"}
        if user_id == None:
            res["code"] = -1
            res["errinfo"] = "invalid args"

        client = tornado.httpclient.AsyncHTTPClient()
        data = yield client.fetch("http://118.89.60.80:8000/recommend/"+user_id)
        if data.code == 200:
            res["data"]=data.body.decode()
        else:
            res["code"]=-1
            res["errinfo"]="data error"
        self.write(res)
        self.finish()
        client.close()
           
class ABTest3(BaseHandler):
    
    executor = ThreadPoolExecutor(5)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self,user_id):
        res={"code":0,"data":"","errinfo":"success"}
        if user_id == None:
            res["code"] = -1
            res["errinfo"] = "invalid args"
        
        client = tornado.httpclient.HTTPClient()
        data = yield self.song_rec(user_id)
        if data.code == 200:
            res["data"]=data.body.decode()
        else:
            res["code"]=-1
            res["errinfo"]="data error"
        self.write(res)
        self.finish()
        client.close()
           
    @run_on_executor
    def song_rec(self,user_id):

        client = tornado.httpclient.HTTPClient()
        data = client.fetch("http://118.89.60.80:8000/recommend/"+user_id)
        return data

        
        

