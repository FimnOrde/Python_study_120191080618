#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class10_exercise1.py
# author:74049
# datetime:2021/4/1 14:32
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os

# os.remove("D:\\PythonTest\\Test\\class10\\class10_exercise1\\text.txt")

path = "D:\\PythonTest\\Test\\class10\\class10_exercise1\\test0"

file_lis = os.listdir(path)

for i in file_lis:
    if os.path.isfile(path + "\\" + i):
        os.remove(path + "\\" + i)
    if os.path.isdir(path + "\\" + i):
        os.removedirs(path + "\\" + i)
print("删除成功")

