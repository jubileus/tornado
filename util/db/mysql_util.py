# coding=UTF-8

import pymysql

__author__ = 'jubileus'


'''
    此工具类用于MySQL的增删改查操作
'''


# 连接数据库
def conn_db(host='192.168.1.33', user='python', passwd='123', db='python', port=3306, charset='utf8'):
    # 获取Connection
    conn = pymysql.connect(host=str(host), user=str(user), passwd=str(passwd), db=str(db), port=int(port),
                           charset=str(charset))
    # 获取Cursor
    cur = conn.cursor()
    return conn, cur


# 关闭数据库
def close_db(conn, cur):
    conn.close()
    cur.close()


# 查询
def query(cur, sql):
    cur.execute(sql)
    return cur.fetchall()


# 插入,更新,删除
def operate(conn, cur, sql):
    stat = cur.execute(sql)
    conn.commit()
    return stat
