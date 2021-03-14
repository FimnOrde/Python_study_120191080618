#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework1.py
# author:74049
# datetime:2021/3/14 13:46
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

even = [i for i in range(0, 51) if i % 2 == 0]
odd = [i for i in range(0, 51) if i % 2 == 1]
lis1 = []
lis2 = [i for i in range(0, 51) if i % 3 == 0 and i % 2 == 0]

# 打印偶数
print("0-50间的偶数")
for i in even:
    print(i, end=' ')
print('\n')

# 打印奇数
print("0-50间的奇数")
for i in odd:
    print(i, end=' ')
print('\n')

# 判断是否为质数
lis1.append(1)
for i in range(3, 51):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lis1.append(i)

# 打印质数
print("0-50间的质数")
for i in lis1:
    print(i, end=' ')
print('\n')

# 打印符合条件数
print("0-50同时被2和3整除的数")
for i in lis2:
    print(i, end=' ')





