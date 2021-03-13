#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class3_exercise.py
# author:74049
# datetime:2021/3/13 13:58
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

lis = []

print("输入五个同学成绩:")
for i in range(0, 5):
    x = input()
    lis.append(int(x))

print("成绩排序:")
lis.sort()
for i in lis:
    print(i, end=' ')
print(end='\n')

print("输入添加的成绩:")
x = input()
lis.append(int(x))
print("添加后成绩排序:")
lis.sort()
for i in lis:
    print(i, end=' ')