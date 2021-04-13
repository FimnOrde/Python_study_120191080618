#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework1.py
# author:74049
# datetime:2021/4/13 15:12
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import time

def metric(func):
    def wrapper(*x):
        start_time = time.time()
        func(*x)
        end_time = time.time()
        exe_time = end_time - start_time
        print(f'函数{func.__name__}()运行时间:', exe_time)
    return wrapper

@metric
def fast(x, y):
    time.sleep(1)
    return x + y;

@metric
def slow():
    time.sleep(5)

fast(11, 22)
slow()