# coding=UTF-8

from util.db import mysql_util
from util.encrypt.md5 import md5

__author__ = 'jubileus'


class User:
    # 定义基本属性
    id = 0
    name = ''
    age = 0
    password = ''

    # 定义方法

    def __init__(self, _name, _age=0, _id=0, _password='123456'):
        self.id = _id
        self.name = _name
        self.age = _age
        self.password = _password

    def info(self):
        print('ID:{_id},  Age:{_age},  Name:{_name}'.format(_id=str(self.id).rjust(5), _name=str(self.name),
                                                            _age=str(self.age).rjust(3)))

    # 查询用户列表（全部用户）
    @staticmethod
    def get_all():
        # 连接数据库
        conn, cur = mysql_util.conn_db()
        # 查询用户列表（全部用户）
        result = mysql_util.query(cur, 'SELECT * FROM t_user')
        u_list = []
        for u in result:
            usr = User(u[1], u[2], u[0], u[3])
            u_list.append(usr)
        # 关闭数据库连接
        mysql_util.close_db(conn, cur)
        return u_list

    # 查询id查询单个用户
    @staticmethod
    def get_by_id(id):
        # 连接数据库
        conn, cur = mysql_util.conn_db()
        # 查询id查询单个用户
        result = mysql_util.query(cur, 'SELECT * FROM t_user WHERE id = {_id}'.format(_id=id))
        if len(result) > 0:
            u = result[0]
            # 关闭数据库连接
            mysql_util.close_db(conn, cur)
            return User(u[1], u[2], u[0], u[3])
        else:
            # 关闭数据库连接
            mysql_util.close_db(conn, cur)
            return None

    # 根据sql更新用户
    @staticmethod
    def execute_sql(sql):
        # 连接数据库
        conn, cur = mysql_util.conn_db()
        # 根据sql更新用户
        result = mysql_util.operate(conn, cur, sql)
        # 关闭数据库连接
        mysql_util.close_db(conn, cur)
        return result

    # 批量添加用户
    @staticmethod
    def batch_insert(users):
        # 连接数据库
        conn, cur = mysql_util.conn_db()
        # 批量添加用户
        sql = "INSERT INTO t_user (name, age, password) VALUES "
        for i in range(len(users)):
            u_name = users[i].name
            u_age = users[i].age
            u_password = md5(users[i].password)
            sql += "('{}','{}','{}')".format(u_name, u_age, u_password) if i == len(
                users) - 1 else "('{}','{}','{}'),".format(u_name, u_age, u_password)
        result = mysql_util.operate(conn, cur, sql)
        # 关闭数据库连接
        mysql_util.close_db(conn, cur)
        return result

    # 保存至数据库
    def save_user(self):
        # 连接数据库
        conn, cur = mysql_util.conn_db()
        # 保存至数据库
        sql = "INSERT INTO t_user (name, age, pass) VALUES ('{_name}','{_age}','{_password}')".format(_name=self.name,
                                                                                                      _age=self.age,
                                                                                                      _password=md5(
                                                                                                          self.password))
        result = mysql_util.operate(conn, cur, sql)
        # 关闭数据库连接
        mysql_util.close_db(conn, cur)
        return result

    # 从数据库删除
    def delete_user(self):
        # 连接数据库
        conn, cur = mysql_util.conn_db()
        # 从数据库删除
        sql = "DELETE FROM t_user WHERE id = {_id}".format(_id=self.id)
        result = mysql_util.operate(conn, cur, sql)
        # 关闭数据库连接
        mysql_util.close_db(conn, cur)
        return result

    # 修改用户属性
    def modify_user(self):
        # 连接数据库
        conn, cur = mysql_util.conn_db()
        # 修改用户属性
        sql = "UPDATE t_user SET name = '{_name}', age = '{_age}', password = '{_password}' WHERE id = {_id}".format(
            _name=str(self.name),
            _age=int(self.age),
            _id=int(self.id),
            _password=str(md5(self.password)))
        result = mysql_util.operate(conn, cur, sql)
        # 关闭数据库连接
        mysql_util.close_db(conn, cur)
        return result

    # 将User对象转化为JSON对象
    def to_json(self):
        return {'id': self.id, 'name': self.name, 'age': self.age}

    # 用户登录
    @staticmethod
    def login(param):
        if param['name'] and param['password']:
            # 连接数据库
            conn, cur = mysql_util.conn_db()
            # 查询用户
            sql = "SELECT * FROM t_user WHERE name = '{_name}' and password = '{_password}'".format(
                _name=str(param['name']),
                _password=str(md5(param['password'])))
            result = mysql_util.query(cur, sql)
            if len(result) > 0:
                u = result[0]
                # 关闭数据库连接
                mysql_util.close_db(conn, cur)
                return User(u[1], u[2], u[0], u[3])
            else:
                # 关闭数据库连接
                mysql_util.close_db(conn, cur)
                return None
        else:
            return None
