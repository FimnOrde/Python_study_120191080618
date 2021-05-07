#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework1.py
# author:74049
# datetime:2021/5/6 16:16
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import random
from concurrent.futures import ThreadPoolExecutor
import threading

mutex = threading.Lock()

def scores(name):
    for i in range(20):
        mutex.acquire()
        print(f'线程{name}生成分数:', random.randint(0, 100))
        mutex.release()

print("5个线程输出100个分数:")
with ThreadPoolExecutor(max_workers=5) as t:
    task1 = t.submit(scores, "1")
    task2 = t.submit(scores, "2")
    task3 = t.submit(scores, "3")
    task4 = t.submit(scores, "4")
    task5 = t.submit(scores, "5")
