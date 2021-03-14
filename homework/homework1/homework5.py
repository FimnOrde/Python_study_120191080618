#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework5.py
# author:74049
# datetime:2021/3/10 17:10
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

import random

lis = [random.randint(1, 50) for i in range(10)]

tup = tuple(random.randint(1, 50) for i in range(10))

print('随机生成的列表:', lis)
print('随机生成的元组:', tup)
