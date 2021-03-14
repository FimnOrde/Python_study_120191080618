#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework2.py
# author:74049
# datetime:2021/3/10 19:52
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

dic = {'19021': 89, '19022': 67, '19023': 98, '19024': 93,
       '19025': 78, '19026': 84, '19027': 90, '19028': 76, '19029': 72, '19020': 81}

print('分数超过80的学生:')

for key in dic:
    if dic[key] > 80:
        print(f'{key}:{dic[key]}')


