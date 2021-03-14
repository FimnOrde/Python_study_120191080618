#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework9.py
# author:74049
# datetime:2021/3/14 13:35
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

n = 5
x0 = 45

print(f'猜测一个整数，一共有{n}次机会')
for i in range(n, 0, -1):
    x = int(input("输入你猜测的数字:"))
    if x == 45:
        print("猜测正确!")
        break
    else:
        if i != 1:
            print(f'猜测错误，你还有{i - 1}次机会')
        else:
            print('猜测失败')



