#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class12_exercise1.py
# author:74049
# datetime:2021/4/13 14:58
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import time, functools

def metric(func):
    def wrapper(x, y, *z):
        return func(x, y, *z)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

else:
    print("f的值为:", f)
    print("s的值为", s)
    print("测试成功")