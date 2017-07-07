from tornado.web import url
from handler.handler import IndexHandler
routes = [
        url(r"/", IndexHandler, name='index')
        ]
