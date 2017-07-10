from tornado.web import url
from handler.handler import *
from handler.login_handler import LoginHandler
routes = [
        url(r"/login", LoginHandler),
        url(r"/song",SongNearHandler)
		url(r"/story", StoryHandler, name='story'),
		url(r"/story/([0-9]+)/up", PraiseHandler, name='praisestory'),
		url(r"/story/([0-9]+)/comment", name='getcomment')
        ]
