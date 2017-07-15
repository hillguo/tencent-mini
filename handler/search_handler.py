from Tools.log import logging
from handler.base_handler import BaseHandler
from model.model import Song

class SearchHandler(BaseHandler):
    def get(self):
        word = '%%{0}%'.format(self.get_argument('word'))
        try:
            results = self.db.query(Song).filter(Song.song_name.like(word)).all()
            self.db.commit()
        except Exception as e:
            logging.error(e)
            self.db.rollback()
            err = {'code': 1, 'errinfo': '查询歌曲失败'}
            self.write(err)
            return

        songsinfo = []
        for row in results:
            singlesong = {'song_id': row.song_id, 'song_name': row.song_name}
            songsinfo.append(singlesong)
        info = {'code': 0, 'data': songsinfo, 'errinfo': 'OK'}
        self.write(info)
