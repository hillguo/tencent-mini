import json
import os
import binascii
import tornado.web
import pymysql
import json

from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound

from Tools.Tools import *


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
            


		
class StoryHandler(BaseHandler)
    def post(self):
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
			info = {'code': 0}
			info_json = json.dumps(info)
			info_encode = info_json.encode('utf-8')
			self.write(info_encode)
		except:
		    db.rollback()
			err = {'code': 1, 'errinfo': '�������ʧ��'}
			err_json = json.dumps(err)
			err_encode = err_json.encode('utf-8')
			self.write(err_encode)
		db.close()
			
class PraiseHandler(BaseHandler)
    def post(self, storyid):
	    postdata = self.request.body.decode('uft-8')
		postdata = json.loads(postdata)
		db = pymysql.connect("595f58f641420.gz.cdb.myqcloud.com", "cdb_outerroot", "mini123456", "tingwen", 5880, use_unicode=True, charset="utf8")
        cursor = db.cursor()
        cursor.execute("SET NAMES utf8")
        cursor.execute("SET CHARACTER SET utf8")
        cursor.execute("SET character_set_connection=utf8")
		sql = '''
		    SELECT * FROM likestory WHERE storyID = {0}
		'''.format(storyid)
		try:
		    cursor.execute(sql)
		except:
			err = {'code': 1, 'errinfo': '��ѯ�û��Ƿ�ϲ������׸���ʱʧ��'}
			err_json = json.dumps(err)
			err_encode = err_json.encode('utf-8')
			self.write(err_encode)
			db.close()
			return
		results = cursor.fetchall()
		if len(results) != 0:
		    err = {'code': 2, 'errinfo': '�Ѿ��������'}
			err_json = json.dumps(err)
			err_encode = err_json.encode('utf-8')
			self.write(err_encode)
			db.close()
			return
			
		sql = '''
		    INSERT INTO likestory(userID, storyID) VALUES({0}, {1})
		'''.format(storyid, postdata['owner_id'])
		try:
		    cursor.execute(sql)
			db.commit()
		except:
		    db.rollback()
			err = {'code': 3, 'errinfo': '"�û�ϲ������"��Ϣ����ʧ��'}
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
			info = {'code': 0}
			info_json = json.dumps(info)
			info_encode = info_json.encode('utf-8')
			self.write(info_encode)
		except:
		    db.rollback()
			err = {'code': 4, 'errinfo': '���µ�����ʧ��'}
			err_json = json.dumps(err)
			err_encode = err_json.encode('utf-8')
			self.write(err_encode)
		db.close()
		
class CommentHandler(BaseHandler)
    def post(self, storyid):
	    db = pymysql.connect("595f58f641420.gz.cdb.myqcloud.com", "cdb_outerroot", "mini123456", "tingwen", 5880, use_unicode=True, charset="utf8")
        cursor = db.cursor()
        cursor.execute("SET NAMES utf8")
        cursor.execute("SET CHARACTER SET utf8")
        cursor.execute("SET character_set_connection=utf8")
		#��ȡ����ID���������ݣ�������ʱ��
	    sql = '''
		    SELECT commentID, content, praisenum, time FROM comment WHERE storyid = {0}
		'''.format(storyid)
		try:
		    cursor.execute(sql)
			db.commit()
			results = cursor.fetchall()
			allstoryinfo = []
			for row in results:
                singlestoryinfo	= {'commentid': row[0], 'content': row[1], 'praisenum': row[2], 'time': row[3]}
				allstoryinfo.append(singlestoryinfo)
			info = {'code': 0, 'data': allstoryinfo}
			storyinfo_json = info.dumps(info)
			storyinfo_encode = storyinfo_json.encode('utf-8')
			self.write(storyinfo_encode)
		except:
		    db.rollback()
			err = {'code': 1, 'errinfo': '��ȡ����ʧ��'}
			err_json = json.dumps(err)
			err_encode = err_json.encode('utf-8')
			self.write(err_encode)
		db.close()
        self.write("hello")




#返回附近的歌曲信息
class SongNearHandler(tornado.web.RequestHandler):
    def get(self):
        latitude = self.get_argument("latitude")
        longitude = self.get_argument("longtitude")

        result = []
        rows = getsonginfo()
        for row in rows:
            if(10 > math.fabs(calculateLineDistance(location(longitude, latitude), location(row["longitude"], row["latitude"])))):
                result.append(row)
        self.finish(json.dump(result))
