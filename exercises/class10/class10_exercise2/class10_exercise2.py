#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class10_exercise2.py
# author:74049
# datetime:2021/4/1 15:15
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os
def copy(srcpath, dstpath):
    if os.path.isfile(srcpath):
        with open(srcpath, 'r', encoding='utf-8')as file:
            lis = file.readlines()
        with open(dstpath, 'w', encoding='utf-8')as file2:
            file2.writelines(lis)
        print("拷贝成功")
    else:
        print("源文件路径有误")

if __name__ == '__main__':
    srcpath = "D:\\PythonTest\\Test\\class10\\class10_exercise2\\src\\text.txt"
    dstpath = "D:\\PythonTest\\Test\\class10\\class10_exercise2\\dst\\text.txt"
    copy(srcpath, dstpath)