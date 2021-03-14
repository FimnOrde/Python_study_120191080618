#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework6.py
# author:74049
# datetime:2021/3/10 17:26
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

a = 0
b = 1

print('100以内的斐波那契数列:', end='')

while True:
    i = a + b
    a = b
    b = i

    if i > 100:
        break

    print(i, end=' ')