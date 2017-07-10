from tornado.web import url
from handler.handler import *

routes = [
        url(r"/", IndexHandler, name='index'),
        url(r"/login", LoginHandler),
        url(r"/userinfo",UserInfoHandler),
        url(r"/song",SongNearHandler)
		url(r"/story", StoryHandler, name='story'),
		url(r"/story/([0-9]+)/up", PraiseHandler, name='praisestory'),
		url(r"/story/([0-9]+)/comment", name='getcomment')
        ]
