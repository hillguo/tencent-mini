import json
from handler.base_handler import BaseHandler
import pymysql

class StoryHandler(BaseHandler):
    def post(self):
	    "留下故事信息"
        postdata = self.request.body.decode('utf-8')
        postdata = json.loads(postdata)
        db = pymysql.connect("595f58f641420.gz.cdb.myqcloud.com", "cdb_outerroot", "mini123456", "tingwen", 5880, use_unicode=True, charset="utf8")
        cursor = db.cursor()
        cursor.execute("SET NAMES utf8")
        cursor.execute("SET CHARACTER SET utf8")
        cursor.execute("SET character_set_connection=utf8")
        sql = '''
		    INSERT INTO story(content, songID, praisenum, longitude, latitude, time, userID)
			VALUES("{0}", {1}, 0, {2}, {3}, "{4}", {5})
		'''.format(postdata['content'], postdata['song_id'], postdata['longitude'], postdata['latitude'], postdata['time'], postdata['owner_id'])
        try:
            cursor.execute(sql)
            db.commit()
            info = {'code': 0, 'errinfo': 'OK'}
            info_json = json.dumps(info)
            info_encode = info_json.encode('utf-8')
            self.write(info_encode)
        except:
            db.rollback()
            err = {'code': 1, 'errinfo': '存入故事失败'}
            err_json = json.dumps(err)
            err_encode = err_json.encode('utf-8')
            self.write(err_encode)
        db.close()
			
class PraiseHandler(BaseHandler):
    def post(self, storyid):
	    "给故事点赞"
        postdata = self.request.body.decode('utf-8')
        postdata = json.loads(postdata)
        db = pymysql.connect("595f58f641420.gz.cdb.myqcloud.com", "cdb_outerroot", "mini123456", "tingwen", 5880, use_unicode=True, charset="utf8")
        cursor = db.cursor()
        cursor.execute("SET NAMES utf8")
        cursor.execute("SET CHARACTER SET utf8")
        cursor.execute("SET character_set_connection=utf8")
        sql = '''
		    SELECT * FROM likestory WHERE userID = {0}
		'''.format(postdata['owner_id'])
        try:
            cursor.execute(sql)
        except:
            err = {'code': 1, 'errinfo': '查询用户是否喜欢过该首歌曲时失败'}
            err_json = json.dumps(err)
            err_encode = err_json.encode('utf-8')
            self.write(err_encode)
            db.close()
            return
        results = cursor.fetchall()
        if len(results) != 0:
            err = {'code': 2, 'errinfo': '已经点过赞了'}
            err_json = json.dumps(err)
            err_encode = err_json.encode('utf-8')
            self.write(err_encode)
            db.close()
            return
			
        sql = '''
		    INSERT INTO likestory(userID, storyID) VALUES({0}, {1})
		'''.format(postdata['owner_id'], storyid)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            err = {'code': 3, 'errinfo': '"用户喜欢故事"信息存入失败'}
            err_json = json.dumps(err)
            err_encode = err_json.encode('utf-8')
            self.write(err_encode)
            db.close()
            return
		
        sql = '''
		    UPDATE story SET praisenum = praisenum + 1 WHERE storyID = {0}
		'''.format(storyid)
        try:
            cursor.execute(sql)
            db.commit()
            info = {'code': 0, 'errinfo': 'OK'}
            info_json = json.dumps(info)
            info_encode = info_json.encode('utf-8')
            self.write(info_encode)
        except:
            db.rollback()
            err = {'code': 4, 'errinfo': '更新点赞数失败'}
            err_json = json.dumps(err)
            err_encode = err_json.encode('utf-8')
            self.write(err_encode)
        db.close()
		
class CommentHandler(BaseHandler):
    def post(self, storyid):
		"获取故事的评论等信息"
        db = pymysql.connect("595f58f641420.gz.cdb.myqcloud.com", "cdb_outerroot", "mini123456", "tingwen", 5880, use_unicode=True, charset="utf8")
        cursor = db.cursor()
        cursor.execute("SET NAMES utf8")
        cursor.execute("SET CHARACTER SET utf8")
        cursor.execute("SET character_set_connection=utf8")
		#获取故事ID，评论内容，点赞数，时间
        sql = '''
		    SELECT commentID, content, praisenum, time FROM comment WHERE storyid = {0}
		'''.format(storyid)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            err = {'code': 1, 'errinfo': '获取评论失败'}
            err_json = json.dumps(err)
            err_encode = err_json.encode('utf-8')
            self.write(err_encode)
            db.close()
            return
        results = cursor.fetchall()
        db.close() 
        allstoryinfo = []
        for row in results:
            singlestoryinfo	= {'commentid': row[0], 'content': row[1], 'praisenum': row[2], 'time': row[3]}
            allstoryinfo.append(singlestoryinfo)
        info = {'code': 0, 'data': allstoryinfo, 'errinfo': 'OK'}
        storyinfo_json = json.dumps(info)
        storyinfo_encode = storyinfo_json.encode('utf-8')
        self.write(storyinfo_encode)