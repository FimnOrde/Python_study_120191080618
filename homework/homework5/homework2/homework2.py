#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework2.py
# author:74049
# datetime:2021/4/13 15:17
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import time

def metric(func):
    def wrapper(*x):
        lis = []
        start_time = time.time()
        num = func(*x)
        end_time = time.time()
        exe_time = end_time - start_time
        lis.append("函数名:" + func.__name__ + '()\n')
        lis.append("函数运行开始时间:" + str(start_time) + '\n')
        lis.append("函数运行结束时间:" + str(end_time) + '\n')
        lis.append("函数运行时间:" + str(exe_time) + '\n')
        lis.append("\n")
        return lis

    return wrapper

@metric
def fast(x, y):
    time.sleep(1)
    return x + y;

@metric
def slow():
    time.sleep(5)

lis1 = fast(11, 22)
lis2 = slow()

with open("D:\\PythonTest\\Test\\homework5\\homework2\\log.txt", 'w', encoding='utf-8')as file:
    file.writelines(lis1)
    file.writelines(lis2)

print("日志写入成功")