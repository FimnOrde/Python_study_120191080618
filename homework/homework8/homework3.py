#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework3.py
# author:74049
# datetime:2021/5/6 16:28
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import multiprocessing
import datetime
import threading

mutex = threading.Lock()

count = 0
index = 0

def primenum(num):
    global count
    global index

    mutex.acquire()
    index += index
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            count += 1
    mutex.release()


if __name__ == '__main__':
    time1 = datetime.datetime.now()
    for num in range(100000):
        primenum(num)
    time2 = datetime.datetime.now()
    exetime = time2 - time1
    print("-"*15, "不使用进程", "-"*15)
    print(exetime)
    print(count)
    count = 0

    time1 = datetime.datetime.now()
    po = multiprocessing.Pool(4)
    for num in range(100000):
        po.apply_async(primenum(num))
    po.close()
    time2 = datetime.datetime.now()
    exetime = time2 - time1
    print("-" * 15, "4个多进程", "-" * 15)
    print(exetime)
    print(count)
    count = 0

    time1 = datetime.datetime.now()
    po1 = multiprocessing.Pool(10)
    for num in range(100000):
        po1.apply_async(primenum(num))
    po1.close()
    time2 = datetime.datetime.now()
    exetime = time2 - time1
    print("-" * 15, "10个多进程", "-" * 15)
    print(exetime)
    print(count)
