#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class_exerxise5.py
# author:74049
# datetime:2021/3/28 17:38
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

with open(r".\aa.txt", "r", encoding='utf-8')as file:
    lis = file.readlines()
lis1 = [0, 78, 87, 83]

seq = zip(lis1, lis)
dic = dict(seq)

diorder = sorted(dic.items(), key = lambda x:x[0])
dic = dict(diorder)

lis0 = [i for i in dic.values()]

with open(r".\bb.txt", "w", encoding='utf-8')as file1:
    lis = file1.writelines(lis0)
