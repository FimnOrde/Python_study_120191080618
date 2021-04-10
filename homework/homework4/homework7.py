#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework7.py
# author:74049
# datetime:2021/4/10 16:14
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os

def getfilelist(srcpath):
    lis = []
    num = 0
    for dir,folder,file in os.walk(srcpath):
        for i in file:
            name = os.path.join(srcpath, i)
            if os.path.isfile(name):
                num += os.path.getsize(name)
    return num

if __name__ == '__main__':
    srcpath = "D:\\PythonTest\\Test\\homework4"
    filesize = getfilelist(srcpath)
    print("文件夹" + srcpath + "中文件的总大小是:" + str(filesize) + "b")