#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework4.py
# author:74049
# datetime:2021/3/30 16:44
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os
try:
    for root, direc, files in os.walk("D:\\PythonTest\\Test\\homework3\\homework4\\img"):
        flis = files
        for i in flis:
            filename = os.path.splitext(i)
            if filename[1] == '.png':
                print(filename[0])
                os.chdir("D:\\PythonTest\\Test\\homework3\\homework4\\img")
                os.rename(i, filename[0] + '.jpg')
except FileExistsError:
        print("写入的文件不存在")
except IOError:
        print("写入时发生错误")
except Exception:
    print("程序发生错误")

