#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class3_exercise.py
# author:74049
# datetime:2021/3/8 13:11
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

stu = ['101','张三','软件1801',[80,89,65]]

print(f'学号:{stu[0]},姓名:{stu[1]}')
print('成绩为:')
for i in stu[3]:
    print(i,end=' ')