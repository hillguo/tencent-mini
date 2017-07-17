import json
import traceback

import tornado.httpclient


from handler.base_handler import BaseHandler          



class SongRecommendHandler(BaseHandler):
    
     @tornado.web.asynchronous
     @tornado.gen.coroutine
     def get(self):
        res={"code":0,"data":"","errinfo":"success"}
        user_id = self.get_argument("user_id",None)
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
           


        
        

