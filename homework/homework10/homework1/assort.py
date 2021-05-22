#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:assort.py
# author:74049
# datetime:2021/5/22 22:40
# software: PyCharm
'''
this is functiondescription
'''
# import module your need


def assort(lis1, lis2, lis3, lis4):
    li1, li2, li3, li4 = [], [], [], []
    for i in lis1:
        li1.append(i['name'])
    for i in lis2:
        li2.append(i['name'])
    for i in lis3:
        li3.append(i['name'])
    for i in lis4:
        li4.append(i['name'])
    print('|男   |', end='')
    for i in li1:
        print(i, end=' ')
    print()
    print('|女   |', end='')
    for i in li2:
        print(i, end=' ')
    print()
    print('|中性   |', end='')
    for i in li3:
        print(i, end=' ')
    print()
    print('|保密   |', end='')
    for i in li4:
        print(i, end=' ')