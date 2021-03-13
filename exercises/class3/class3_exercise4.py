#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class3_exercise3.py
# author:74049
# datetime:2021/3/9 16:29
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 元组的基本操作
tup0 = ('r', 'u', 'n', 'o', 'o', 'b','Google', 'FireFox')
tup1 = (1997, 2000, 56, 12)

# 基本运算
print('元组拼接:', tup0 + tup1)
print('元组复制:', tup1 * 3)
print('元素存在判断:', 'Google' in tup0)
print('迭代:', end='')
for i in tup0:
    print(i, end=' ')

# 内置函数
print('元组长度:', len(tup0))
print('元组最大值:', max(tup1))
print('元组最小值:', min(tup1))
print('元组和:', sum(tup1))