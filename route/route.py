from tornado.web import url
from handler.login_handler import LoginHandler, UserInfoHandler
from handler.near_song_handler import SongNearHandler
from handler.song_story_handler import SongStoryHandler
from handler.story_handler import StoryHandler, PraiseHandler, CommentHandler
routes = [
        url(r"/login", LoginHandler),
        #url(r"/song",SongNearHandler),
		url(r"/story", StoryHandler, name='story'),
		url(r"/story/([0-9]+)/up", PraiseHandler, name='praisestory'),
		url(r"/story/([0-9]+)/comment", CommentHandler, name='getcomment'),
        url(r"/userinfo",UserInfoHandler),
        url(r"/song/near", SongNearHandler),
        url(r"/song/story", SongStoryHandler)
        ]
