#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class8_exercise1.py
# author:74049
# datetime:2021/3/27 10:30
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os

print("class8_exercise1.py文件路径为:",
      os.path.dirname("D:\\PythonTest\\Test\\class8\\class8_exercise1\\class8_exercise1.py"))

# print("在指定目录创建新目录", end="")
# os.mkdir("D:\\PythonTest\\Test\\class8\\class8_exercise1\\test_mkdir")

print("D:\\PythonTest\\Test\\class8目录下的文件有:")
for root, dirs, files in os.walk("D:\\PythonTest\\Test\\class8"):
    print(files)


