#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class3_exercise2.py
# author:74049
# datetime:2021/3/8 14:59
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
scores = [65,95,85,84,76,94,64,71,91,65]

print(f'最高分:{max(scores)}')
print(f'最低分:{min(scores)}')
print(f'总分:{sum(scores)}')
print(f'平均分:{sum(scores) / len(scores)}')