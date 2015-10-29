# coding=UTF-8

import tornado.ioloop
import tornado.web

__author__ = 'jubileus'


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get_current_user(self):
        return self.get_secure_cookie("u_id")
