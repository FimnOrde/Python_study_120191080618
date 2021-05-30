#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework11.py
# author:74049
# datetime:2021/5/28 21:36
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from flask import Flask, render_template, request, redirect
import pymysql
from flask_bootstrap import Bootstrap
from database_oper import do_infomodel


# 创建flask应用对象
app = Flask(__name__)

bootstrap = Bootstrap(app)

userlis = []
num = 0

@app.route('/get')
def userlist2():
    global userlis, num
    conn = pymysql.connect(host='localhost', user='root', password='648175', db='to_do', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM todolist"
    cur.execute(sql)
    userlist = cur.fetchall()  # 数据集为返回一个嵌套元组
    conn.close()
    num = int(userlist[-1][0])
    return render_template('users.html', u=userlist)

@app.route('/get', methods=['POST'])
def login():
    global userlis, num
    if request.method =='POST':
        userlis = []
        username = request.form['username']
        done = request.form['1']
        edit = request.form['2']
        edit2 = request.form['21']
        remove = request.form['3']
        password = request.form['password']

        if username != "":
            info = do_infomodel.query_condition_opa(username)
            for i in info:
                userlis.append(tuple(i.values()))
            #userlis.append(tuple(info[0].values()))
            return render_template('users.html', u=userlis)

        elif password != '':
            do_infomodel.test_add(password, num)
            conn = pymysql.connect(host='localhost', user='root', password='648175', db='to_do', charset='utf8')
            cur = conn.cursor()
            sql = "SELECT * FROM todolist"
            cur.execute(sql)
            userlist = cur.fetchall()  # 数据集为返回一个嵌套元组
            conn.close()
            num = int(userlist[-1][0])
            return render_template('users.html', u=userlist)

        elif done != '':
            do_infomodel.test_udd(done, 0)
            conn = pymysql.connect(host='localhost', user='root', password='648175', db='to_do', charset='utf8')
            cur = conn.cursor()
            sql = "SELECT * FROM todolist"
            cur.execute(sql)
            userlist = cur.fetchall()  # 数据集为返回一个嵌套元组
            conn.close()
            num = int(userlist[-1][0])
            return render_template('users.html', u=userlist)

        elif remove != '':
            do_infomodel.test_dle(remove)
            conn = pymysql.connect(host='localhost', user='root', password='648175', db='to_do', charset='utf8')
            cur = conn.cursor()
            sql = "SELECT * FROM todolist"
            cur.execute(sql)
            userlist = cur.fetchall()  # 数据集为返回一个嵌套元组
            conn.close()
            num = int(userlist[-1][0])
            return render_template('users.html', u=userlist)

        elif edit != '':
            do_infomodel.test_udd(edit, edit2)
            conn = pymysql.connect(host='localhost', user='root', password='648175', db='to_do', charset='utf8')
            cur = conn.cursor()
            sql = "SELECT * FROM todolist"
            cur.execute(sql)
            userlist = cur.fetchall()  # 数据集为返回一个嵌套元组
            conn.close()
            num = int(userlist[-1][0])
            return render_template('users.html', u=userlist)


        else:
            message = "Failed Login"
            return render_template('users.html',message=message)

    return render_template('users.html')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
