#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class8_exercise2.py
# author:74049
# datetime:2021/3/28 16:57
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

with open(r".\xxx.txt", "w")as file1:
    file1.write("write in the same level")

with open(r".\a_file\aa.txt", "w")as file2:
    file2.write("write in the sublevel")

with open(r"..\class8_exercise1\aa.txt", "w")as file3:
    file3.write("write in the suplevel")
