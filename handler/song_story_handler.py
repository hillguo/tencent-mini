import json
from handler.base_handler import BaseHandler


#返回歌曲的故事信息
class SongStoryHandler(BaseHandler):
    def get(self):
        #if(not self.valid_user()):
        songid= self.get_argument("songid")
        rep = {"code": 0, "data": None}

        try:
            sql = "select * from story where songID = " + str(songid)
            rows = self.db.execute(sql).fetchall()
            result = []
            for row in rows:
                tmp = {}
                tmp["longitude"] = row["longitude"]
                tmp["latitude"] = row["latitude"]
                tmp["story_id"] = row["storyID"]
                tmp["content"] = row["content"]
                tmp["user_id"] = row["userID"]
                result.append(tmp)
            rep["data"] = result
        except:
            rep["code"] = -1
            rep["errinfo"] = "something error"

        self.finish(json.dumps(rep))
