# -*- coding: UTF-8 -*-

import json
from handler.base_handler import BaseHandler
from Tools.tools import *
from Tools.log import logging
import math

#返回附近的歌曲信息
class SongNearHandler(BaseHandler):
    def get(self):
        #if(not self.valid_user()):
        rep = {"code": 0, "errinfo": "success"}

        try:
            latitude = self.get_argument("latitude")
            longitude = self.get_argument("longitude")
        except Exception as e:
            rep["code"] = 3
            rep["errinfo"] = "请求参数有问题"
            logging.error(e)
            self.finish(json.dumps(rep ,ensure_ascii=False))

        try:
            sql = "select story_id,song_id,longitude, latitude from story"
            rows = self.db.execute(sql).fetchall()
        except Exception as e:
            rep["code"] = 1
            rep["errinfo"] = "数据库查询失败"
            logging.error(e)
            self.finish(json.dumps(rep ,ensure_ascii=False))

        try:
            result = []
            for row in rows:
                if(100000 > math.fabs(calculateLineDistance(location(longitude, latitude),
                                                        location(row["longitude"], row["latitude"])))):
                    tmp_dic = {}
                    tmp_dic["longitude"] = row["longitude"]
                    tmp_dic["latitude"] = row["latitude"]
                    tmp_dic["song_id"] = row["song_id"]
                    tmp_dic["story_id"] = row["story_id"]
                    result.append(tmp_dic)
            rep["data"] = result
            rep["errinfo"] = "success!!"
        except Exception as e:
            rep["code"] = 2
            rep["errinfo"] = "数据库没有对应的字段"
            logging.error(e)
            self.finish(json.dumps(rep ,ensure_ascii=False))

        self.finish(json.dumps(rep ,ensure_ascii=False))


