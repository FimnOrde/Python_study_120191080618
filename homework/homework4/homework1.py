#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework1.py
# author:74049
# datetime:2021/4/6 14:14
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from collections import deque
import time

try:
    print("程序开始时间:", time.time())
    t = time.time()

    lis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("初始列表:",  lis)
    qlis = deque(lis)
    qlis.append(10)
    qlis.appendleft(-1)

    print("添加元素后列表:", list(qlis))
    print("程序结束时间:", time.time())
    print("程序运行时间:", time.time() - t)
except Exception:
    print("程序出错")