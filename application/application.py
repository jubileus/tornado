# coding=UTF-8

import os

import tornado.ioloop
import tornado.web

from url.url import url

__author__ = 'jubileus'

setting = dict(
    template_path=os.path.join(os.path.dirname(__file__), "template"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    login_url="/login"
    )

application = tornado.web.Application(
    handlers=url,
    **setting
    )
