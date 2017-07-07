# -*- coding:utf-8 -*_

import os
import logging

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from config import config
from route import route

import database.init_db

class Application(tornado.web.Application):
    def __init__(self):
        handlers = route.routes
        settings = dict(
                cookie_secret = options.cookie_secret,
                login_url = options.login_url,
                template_path = options.template_path,
                static_path = options.static_path,
                xsrf_cookies = options.xsrf_cookies,
                debug = options.debug
                )
        super(Application,self).__init__(handlers,**settings)
        engine=create_engine(options.db_path,convert_unicode=True,echo=options.debug)
        #database.init_db.init_db(engine)
        self.db=scoped_session(sessionmaker(bind=engine))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  
    app = Application()
    app.listen(options.port)
    consoleStr = "server is running, listen port:(0),runningEnv:{1}".format(options.port,options.env)
    logging.info(consoleStr)
    tornado.ioloop.IOLoop.instance().start()
