# coding=UTF-8

import tornado.web

from handler.base_handler import BaseHandler

from entity.t_user import User

__author__ = 'jubileus'


class UserHandler(BaseHandler):
    # def prepare(self):
    #     info('path = ' + str(self.request.path))

    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self, user_id):
        user = User.get_by_id(user_id)
        json = {}
        if user:
            json['msg'] = 'OK'
            json['code'] = 200
            json['data'] = user.to_json()
        else:
            json['msg'] = '该用户ID不存在'
            json['code'] = -1
        self.render("user_index.html", info=json)
