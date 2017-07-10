from tornado.web import url
from handler.handler import *

routes = [
        url(r"/", IndexHandler, name='index'),
        url(r"/login", LoginHandler),
        url(r"/userinfo",UserInfoHandler),
        url(r"/song",SongNearHandler)
        ]
