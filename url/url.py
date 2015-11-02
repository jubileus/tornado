# coding=UTF-8

from handler.user_handler import UserHandler
from handler.login_handler import LoginHandler
from handler.file_handler import UploadFileHandler
from handler.file_handler import FileHandler
from handler.file_handler import DownloadFileHandler

__author__ = 'jubileus'

url = [
    (r'/user/([0-9]+)', UserHandler),
    (r'/login', LoginHandler),
    (r'/file', FileHandler),
    (r'/upload', UploadFileHandler),
    (r'/download', DownloadFileHandler)
]
