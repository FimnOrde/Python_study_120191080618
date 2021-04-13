#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class12_exercise2.py
# author:74049
# datetime:2021/4/13 14:29
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import time

def metric(func):
    def wrapper(x, y):
        start_time = time.time()
        num = func(x, y)
        end_time = time.time()
        exe_time = end_time - start_time
        print("程序运行开始时间:", start_time)
        print(f'{x}+{y} =', num)
        print("程序运行结束时间:", end_time)
        print("运行时间:", exe_time)
    return wrapper

@metric
def fast(x, y):
    time.sleep(1)
    return x + y;

fast(11, 22)
