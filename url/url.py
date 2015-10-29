# coding=UTF-8

from handler.user_handler import UserHandler
from handler.login_handler import LoginHandler

__author__ = 'jubileus'

url = [
    (r'/user/([0-9]+)', UserHandler),
    (r'/login', LoginHandler)
]
