#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:read_from_db.py
# author:74049
# datetime:2021/5/26 15:51
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

from flask import Flask,render_template
import pymysql
from flask_bootstrap import Bootstrap

# 创建flask应用对象
app=Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return 'this is my web-flask index page!'

@app.route('/users2')
def userlist2():
    conn = pymysql.connect(host='localhost', user='root', password='648175', db='to_do', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM todolist"
    cur.execute(sql)
    userlist = cur.fetchall()  # 数据集为返回一个嵌套元组
    conn.close()
    return render_template('users.html',u=userlist)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5001)