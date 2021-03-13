#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class4_exercise4.py
# author:74049
# datetime:2021/3/13 16:02
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

x = input()

xtuple = x.split()
xtuple = tuple([xtuple[i] for i in range(len(xtuple))])

print(xtuple)