#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class5_exercise3.py
# author:74049
# datetime:2021/3/17 15:26
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

def recursfib(n):
    if n == 1:
        return 0

    elif n ==2:
        return 1

    else:
        return recursfib(n-1)+recursfib(n-2)

def fibcom(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

if __name__ == '__main__':
    print("前20个斐波那契数列(递归):")

    for i in range(1, 21):
        print(recursfib(i), end=" ")

    print("\n前20个斐波那契数列(递推):")
    fibcom(20)