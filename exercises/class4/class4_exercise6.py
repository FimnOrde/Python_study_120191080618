#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class4_exercise6.py
# author:74049
# datetime:2021/3/16 15:14
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

import random

lis = [random.randint(0, 50) for i in range(10)]


print("列表为:", lis)
print("其中的偶数有:")

for i in lis:
    if i % 2 == 0:
        print(i, end=" ")

