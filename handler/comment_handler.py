import json
from datetime import datetime

from model.model import Comment, Story
from handler.base_handler import BaseHandler

class CommentHandler(BaseHandler):

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
        story = self.db.query(Story).filter(Story.id == story_id).first()
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

