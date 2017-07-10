import json
import pymysql
import time
with open('story.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

db = pymysql.connect("595f58f641420.gz.cdb.myqcloud.com", "cdb_outerroot", "mini123456", "tingwen", 5880, use_unicode=True, charset="utf8")
cursor = db.cursor()
cursor.execute("SET NAMES utf8")
cursor.execute("SET CHARACTER SET utf8")
cursor.execute("SET character_set_connection=utf8")
i=1;
for songinfo in data:
    sql = '''
        INSERT INTO story(storyID, content, songID, praisenum, longitude, latitude, time)
        VALUES({0}, "{1}", "{2}", "{3}", "{4}", "{5}", "{6}")
	    '''.format(songinfo['story_id'] + i, songinfo['content'] + str(i), songinfo['song_id'], songinfo['praisenim'], songinfo['longitude'], songinfo['latitude'],time.time())
    try:
        cursor.execute(sql)
        db.commit()
        i = i+1
    except :
        db.rollback()
        print("insert database error")
#print(sql)
db.close()
