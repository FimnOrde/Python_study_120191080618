#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework10.py
# author:74049
# datetime:2021/3/14 15:52
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from operator import itemgetter

text = input("输入一段英文文本:")
dic = {}

lis = text.split(" ")

for i in lis:
    if i !=" ":
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] = dic[i]+1



sdic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
dic1 = dict(sdic)

print("词汇统计:")
for i in dic1:
    print(f'{i}:{dic1[i]}')


