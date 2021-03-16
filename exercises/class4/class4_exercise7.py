#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class4_exercise7.py
# author:74049
# datetime:2021/3/16 16:27
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
L = ['Hello', 'World', 18, 'Apple', None]

L1 = [s.lower() for s in L if isinstance(s, str) == True]

print(L1)
