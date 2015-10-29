# coding=UTF-8

import hashlib

__author__ = 'jubileus'


# 获取字符串的md5值
def md5(s):
    if isinstance(s, str):
        m = hashlib.md5()
        m.update(s.encode('utf8'))
        return m.hexdigest()
    else:
        return ''
