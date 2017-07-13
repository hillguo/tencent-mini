import json
import logging
from handler.base_handler import BaseHandler

class SearchHandler(BaseHandler):
    def get(self):
        word = self.get_argument('word')
        print(word)
        sql = """
            SELECT song_id, song_name FROM song WHERE song_name LIKE '%{0}%'
        """.format(word)
        try:
            results = self.db.execute(sql).fetchall()
            self.db.commit()
        except Exception as e:
            logging.error(e)
            self.db.rollback()
            err = {'code': 1, 'errinfo': '查询歌曲失败'}
            self.write(err)
            return

        songsinfo = []
        for row in results:
            singlesong = {'song_id': row[0], 'song_name': row[1]}
            songsinfo.append(singlesong)
        info = {'code': 0, 'data': songsinfo, 'errinfo': 'OK'}
        self.write(info)