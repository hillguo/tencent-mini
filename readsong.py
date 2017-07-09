import json
import pymysql
with open('songs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

db = pymysql.connect("595f58f641420.gz.cdb.myqcloud.com", "cdb_outerroot", "mini123456", "tingwen", 5880, use_unicode=True, charset="utf8")
cursor = db.cursor()
cursor.execute("SET NAMES utf8")
cursor.execute("SET CHARACTER SET utf8")
cursor.execute("SET character_set_connection=utf8")

for songinfo in data:
    sql = '''
        INSERT INTO song(songID, songLink, lrcLink, songPicSmall, songName, tag)
        VALUES({0}, "{1}", "{2}", "{3}", "{4}", "{5}")
	    '''.format(songinfo['id'], songinfo['songLink'], songinfo['lrcLink'], songinfo['songPicSmall'], songinfo['songName'], songinfo['tag'])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print("insert database error")
#print(sql)
db.close()