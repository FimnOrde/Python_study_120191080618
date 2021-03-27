#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework3.py
# author:74049
# datetime:2021/3/27 15:20
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import random

def oddnum(lis):
    for i in lis:
        if i % 2 == 1:
            print(i, end=" ")

if __name__ == '__main__':
    lis = [random.randint(1, 50) for i in range(10)]
    print("数字列表为:", lis)
    print("列表中奇数为:", end="")
    oddnum(lis)
