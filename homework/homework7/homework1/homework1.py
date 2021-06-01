#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework1.py
# author:74049
# datetime:2021/5/23 21:38
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import re

def Find(string):
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{homework2}))+', string)
    return url

str = ''

try:
    with open('D:\\PythonTest\\Test\\homework7\\homework1\\webspiderUrl.txt', 'r', encoding='utf-8') as file:
        lis = file.readlines()

    for i in lis:
        str += i

    url = Find(str)

    print('文件读取成功')

except Exception:
    print('文件读取错误')

try:
    with open('D:\\PythonTest\\Test\\homework7\\homework1\\extracts.txt', 'w', encoding='utf-8') as file:
        for i in url:
            file.write(i)
            file.write('\n')

    print('文件写入成功')

except Exception:
    print('文件写入错误')