from tornado.web import url
from handler.handler import *
routes = [
        url(r"/", IndexHandler, name='index'),
        url(r"/login", LoginHandler)
        ]
