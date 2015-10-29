# coding=UTF-8

from handler.base_handler import BaseHandler

from entity.t_user import User

__author__ = 'jubileus'


class LoginHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('login.html')

    def post(self):
        user = User.login({'name': self.get_argument('username'), 'password': self.get_argument('password')})
        if user:
            self.set_secure_cookie("u_id", str(user.id))
            self.redirect('/user/' + str(user.id))
        else:
            self.redirect('/login')
