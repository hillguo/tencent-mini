import json
from handler.base_handler import BaseHandler
from Tools.tools import *
import math

#返回附近的歌曲信息
class SongNearHandler(BaseHandler):
    def get(self):
        #if(not self.valid_user()):
        latitude = self.get_argument("latitude")
        longitude = self.get_argument("longitude")

        #rep = {"code" :0, "data":None,"errinfo":"success"}
        rep = {}
        try:
            sql = "select songID,longitude, latitude from story"
            rows = self.db.execute(sql).fetchall()
            result = []
            for row in rows:
                if(10 > math.fabs(calculateLineDistance(location(longitude, latitude), location(row["longitude"], row["latitude"])))):
                    tmp = {}
                    tmp["longitude"] = row["longitude"]
                    tmp["latitude"] = row["latitude"]
                    tmp["song_id"] = row["songID"]
                    result.append(tmp)
            rep["data"] = result
            rep["errinfo"] = "success!!"
        except:
            rep["code"] = -1
            rep["errinfo"] = "something error"

        print(rep)
        self.finish(json.dumps(rep))

