#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework7.py
# author:74049
# datetime:2021/3/14 14:22
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
for i in range(1, 10):
    for j in range(1, 10):
        if i > j:
            print(f'{j}×{i}={i*j}', end='  ')
        elif i == j:
            print(f'{j}×{i}={i * j}')
