from tornado.web import url
from handler.handler import *
from handler.login_handler import LoginHandler
routes = [
        url(r"/login", LoginHandler),
        url(r"/song",SongNearHandler)
        ]
