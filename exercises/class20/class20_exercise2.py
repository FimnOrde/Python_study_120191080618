#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class20_exercise2.py
# author:74049
# datetime:2021/5/14 19:02
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import re
text = input("Please input your Email address：\n")
if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',text):
    print('Email address is Right!')
else:
    print('Please reset your right Email address!')