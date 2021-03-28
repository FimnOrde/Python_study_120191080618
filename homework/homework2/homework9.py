#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework9.py
# author:74049
# datetime:2021/3/28 19:53
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import random

def arrsort(array):
    array.sort()
    return array

if __name__ == '__main__':
    lis = [random.randint(1, 200) for i in range(20)]
    print("原数组:", lis)
    print("排序后:", arrsort(lis))