# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/5/18 15:48'

import threading
from functools import wraps
import pymysql
from pymysql.err import Error


# 单例装饰器
def Singleton(cls):
    """线程安全的单例装饰器"""
    instance = {}
    lock = threading.Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            with lock:
                if cls not in instance:
                    instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper


# 单例类
class Sigleton(type):
    """线程安全的单例元类"""
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.__lock = threading.Lock()

        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance

# @Singleton
# class Dao(object):
#     pass


class Dao(metaclass=Sigleton):
    """数据库操作类"""

    def __init__(self,user,password,database,host='localhost',port=3306,charset='utf8'):
        '''
        初始化数据库实例
        :param user: 用户名
        :param password: 密码
        :param database: 数据库
        :param host: 主机名
        :param port: 端口
        :param charset: 字符集
        '''
        self._host = host
        self._user = user
        self._password = password
        self._port = port
        self._database = database
        self._charset = charset
        self._connection = pymysql.connect(host= self._host,
                                     user= self._user,
                                     password= self._password,
                                     db= self._database,
                                     charset= self._charset)

    def insert(self, table, data):
        '''
        插入数据
        :param table: 表名
        :param data: 数据字典
        :return: 成功True，失败False
        '''
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'insert into {table}({keys})values({values})'.format(table=table,keys=keys,values=values)
        try:
            with self._connection.cursor() as cursor:
                if cursor.execute(sql, tuple(data.values())):
                    self._connection.commit()
                    return True
        except Error as e:
            self._connection.rollback()
            return (False, e.args)

    def delete(self, table, condition):
        '''
        删除数据
        :param table: 表名
        :param condition: 删除条件
        :return: 成功True,失败False
        '''
        sql = "delete from {table} where {condition}".format(table=table,condition=condition)
        try:
            with self._connection.cursor() as cursor:
                if cursor.execute(sql):
                    self._connection.commit()
                    return True
        except Error as e:
            self._connection.rollback()
            return (False, e.args)

    def update(self, table, data):
        '''
        修改数据
        :param table: 表名
        :param data: 修改数据
        :return: 成功True,失败False
        '''
        keys = ','.join(data.keys())
        values = ','.join(['%s']*len(data))
        sql = "insert into {table}({keys})values({values}) on duplicate key update".format(table=table, keys=keys, values=values)
        update = ','.join([' {key}=%s'.format(key=key) for key in data.keys()])
        sql +=update
        try:
            with self._connection.cursor() as cursor:
                if cursor.execute(sql, tuple(data.values())*2):
                    self._connection.commit()
                    return True
        except Error as e:
            self._connection.rollback()
            return (False, e.args)

    def fetchone(self, sql):
        '''
        查询数据
        :param sql: sql语句
        :return: 查询结果
        '''
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(sql)
                data = cursor.fetchone()
                if data:
                    return data
                return False
        except Error as e:
            return (False, e.args)

    def fetchall(self, sql):
        '''
        查询数据
        :param sql: sql语句
        :return: 查询结果
        '''
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(sql)
                data = cursor.fetchone()
                while data:
                    yield data
                    data = cursor.fetchone()
        except Error as e:
            # return (False, e.args)
            print(e.args)
            # return False


def main():
    dao = Dao('root', '123456', 'db01')
    sql = "select * from stu1;"
    res = dao.fetchone(sql)
    print(res)
    for i in res:
        print(i)


if __name__ == '__main__':
    main()

