#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:connector.py
# author:74049
# datetime:2021/5/22 22:47
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import pymysql

def cnc():
    # 打开数据库连接
    db = pymysql.connect(host="localhost",  # 主机名
                         user="root",  # 用户名
                         password="648175",  # 密码
                         db='commenting',  # 数据库

                         )

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")

    return db, cursor