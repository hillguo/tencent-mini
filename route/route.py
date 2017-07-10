from tornado.web import url
from handler.handler import IndexHandler
from handler.handler import StoryHandler
from handler.handler import PraiseHandler
routes = [
        url(r"/", IndexHandler, name='index'),
		url(r"/story", StoryHandler, name='story'),
		url(r"/story/([0-9]+)/up", PraiseHandler, name='praisestory')
		url(r"/story/([0-9]+)/comment", name='getcomment')
        ]
