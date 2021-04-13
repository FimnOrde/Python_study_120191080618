#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework3.py
# author:74049
# datetime:2021/4/13 15:55
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import time

def metric(func):
    def wrapper(*x):
        account = input("输入函数账号:")
        paassword = input("输入函数密码:")
        if account == 'root':
            if paassword == '123654':
                print(f'函数{func.__name__}()调用成功')
                func(*x)
            else:
                print("密码错误")
        else:
            print("账号有误")


    return wrapper

@metric
def fast(x, y):
    print("函数fast()的内容实现")
    return x + y;

@metric
def slow():
    print("函数slow()的内容实现")

print("尝试调用fast()")
fast(11, 22)
print("尝试调用slow()")
slow()