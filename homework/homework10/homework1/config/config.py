#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:config.py
# author:74049
# datetime:2021/5/20 14:37
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import pymysql
# 数据库连接定义
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:648175@localhost:3306/student_info?charset=utf8"

# 数据库连接池初始化的容量
POOL_SIZE = 5

# 连接池最大溢出容量，该容量+初始容量=最大容量。超出会堵塞等待，等待时间为timeout参数值默认30
MAX_OVERFLOW = 10