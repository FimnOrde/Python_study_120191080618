#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class23_exercise1.py
# author:74049
# datetime:2021/5/24 21:35
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'this is my web-flask index page!'

@app.route('/myweb')
def myweb():
    return '''
    <html>
    <head>
    <title>Hello</title>
    </head>
    <body>
    <h1>Hello, world!</h1><br><br>
    <a href='/' target="_blank">这个是超链接</a>

    </body>
    </html>
'''


# 读取路由中的参数
@app.route('/user/<username>')
def show_user_profile(username):
    return 'hello : %s' % username


if __name__ == '__main__':
    app.run(debug=True,port=5000)
