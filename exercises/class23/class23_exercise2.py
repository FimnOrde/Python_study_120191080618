#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class12_exercise2.py
# author:74049
# datetime:2021/5/24 22:02
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    return 'this is my web-flask index page!'

@app.route('/hello')
def hello():
    return render_template('hello.htm')

@app.route('/hellodata')
def hellodata():
    user_name = 'Jackiex'
    return render_template('hellodata.htm', name=user_name)

@app.route('/data')
def data():
    class Person(object):
        Email = 'XXX@XXX.com';
        time = time.time();

    dell = Person()

    context = {
        'username': "FimOrd",
        'age': "18",
        'gender': "男",
        'flag': "王者",
        'hero': "猴子",
        'person': dell,
        'wwwurl': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }

    return render_template('datas.htm', **context)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)