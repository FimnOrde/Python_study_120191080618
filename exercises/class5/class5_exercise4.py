#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class5_exercise4.py
# author:74049
# datetime:2021/3/15 14:46
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import random

lis = [random.randint(1, 20) for i in range(10)]
print("列表为:", lis)


seq = filter((lambda x: x % 2 == 1) ,lis)
print("列表中奇数为:", list(seq))
