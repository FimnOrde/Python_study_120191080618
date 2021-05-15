#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class21_exercise3.py
# author:74049
# datetime:2021/5/15 11:09
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import mysql.connector

# 数据库操作代码一般结构
conn = mysql.connector.connect(host="localhost", user="root", password="648175", database="user")
#
cursor = conn.cursor()
#
# 创建user表:
#cursor.execute('create table test_user (id varchar(20) primary key, name varchar(20))')

# # 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user_info(id, name) values (%s, %s)', ('4', 'Ally'))
print('rowcount =', cursor.rowcount)
#
# # 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user_info where id = %s', ('1',))
values = cursor.fetchall()
print(values)

# 关闭Cursor和Connection:
cursor.close()
conn.close()