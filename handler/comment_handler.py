import json
from datetime import datetime

from model.model import Comment, Story
from handler.base_handler import BaseHandler

class CommentHandler(BaseHandler):
    def get(self, story_id):
        '''获取故事的评论等信息'''
        #获取故事ID，评论内容，点赞数，时间
        sql = '''
            SELECT comment_id, content, praisenum, time FROM comment WHERE story_id = {0}
        '''.format(story_id)
        try:
            results = self.db.execute(sql).fetchall()
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            err = {'code': 1, 'errinfo': '获取评论失败'}
            self.write(err)
            return

        allstoryinfo = []
        for row in results:
            singlestoryinfo	= {'comment_id': row[0], 'content': row[1], 'up': row[2], 'time': row[3]}
            allstoryinfo.append(singlestoryinfo)
        info = {'code': 0, 'data': allstoryinfo, 'errinfo': 'OK'}
        self.write(info)

    def post(self, story_id):
        res = {
            'code': 0,
            'erroinfo': 'ok'
        }

        content = self.get_argument('content', None)
        
        print(self.request.body)

        if story_id is None:
            res['code'] = 1
            res['errinfo'] = '未提供故事id'
            self.write(res)
            return None
        story = self.db.query(Story).filter(Story.story_id == story_id).first()
        if story is None:
            res['code'] = 2
            res['errinfo'] = '故事不存在'
            self.write(res)
            return None

        comment = Comment(
            content=content,
            story_id=story_id,
            up=0,
            created_at=datetime.utcnow()
        )

        self.db.add(comment)
        self.db.commit()

        self.write(res)
