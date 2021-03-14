#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework3.py
# author:74049
# datetime:2021/3/10 16:59
# software: PyCharm
'''
this is functiondescription
'''
# import module your need


lis0 = [0, 1, 5, 4, 'a', 'b', 'c', 'd']
lis1 = [8, 1, 5, 6, 7, 'c', 'd', 'e']

lis = [i for i in lis0 if i in lis1]

print('两个列表相同元素为:', end=' ')
for i in lis:
    print(i, end=' ')

