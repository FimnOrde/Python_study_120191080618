#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class21_exercise2.py
# author:74049
# datetime:2021/5/15 10:38
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="648175", database="user")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO user_info(name, id)
         VALUES ('cynthia', '3')"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except Exception as e:
   raise e
   print("发生异常",e)


finally:
   db.close()


