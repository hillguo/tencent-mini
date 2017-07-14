import json
from handler.base_handler import BaseHandler
from Tools.log import logging

#返回歌曲的故事信息
class SongStoryHandler(BaseHandler):
    def get(self):
        #if(not self.valid_user()):
        rep = {"code": 0, "errinfo": "success"}
        try:
            song_id = self.get_argument("song_id")
        except Exception as e:
            rep["code"] = 3
            rep["errinfo"] = "请求参数有问题"
            logging.error(e)
            self.finish(json.dumps(rep))

        try:
            sql = "select * from story where song_id = " + str(song_id)
            rows = self.db.execute(sql).fetchall()
        except Exception as e:
            rep["code"] = 1
            rep["errinfo"] = "数据查询失败"
            logging.error(e)
            self.finish(json.dumps(rep))

        try:
            result = []
            for row in rows:
                sql = '''select user_name from user where user_id = "{0}"'''.format(row['user_id'])
                user_row = self.db.execute(sql).fetchone()

                tmp_dic = {}
                tmp_dic["longitude"] = row["longitude"]
                tmp_dic["latitude"] = row["latitude"]
                tmp_dic["story_id"] = row["story_id"]
                tmp_dic["content"] = row["content"]
                tmp_dic["user_id"] = row["user_id"]
                tmp_dic["user_name"] = user_row["user_name"]
                result.append(tmp_dic)

            rep["data"] = result
            rep["code"] = 0
            rep["errinfo"] = "success"
        except Exception as e:
            rep["code"] = 2
            rep["errinfo"] = "数据库没有对应的字段"
            logging.error(e)
            self.finish(json.dumps(rep))

        self.finish(json.dumps(rep))
