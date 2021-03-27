#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework2.py
# author:74049
# datetime:2021/3/27 15:06
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

def compute():
    lis = input("请输入几个数:").split()
    sum = 0
    for i in lis:
         sum = float(i) + sum
    return sum

if __name__ == '__main__':
    print("输入数字的和为:", compute())