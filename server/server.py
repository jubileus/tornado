# coding=UTF-8

from application.application import application

import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.options import define, options

__author__ = 'jubileus'

define("port", default=8888, help="run on th given port", type=int)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print('Development server is running at http://localhost:{}/'.format(options.port))
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
