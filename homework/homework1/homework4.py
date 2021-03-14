#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework4.py
# author:74049
# datetime:2021/3/10 17:18
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

inp = int(input('输入一个年份:'))

if inp % 4 == 0:
    print(f'{inp}年是闰年')
else:
    print(f'{inp}年不是闰年')

