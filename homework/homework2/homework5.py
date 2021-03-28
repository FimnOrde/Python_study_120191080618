#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework5.py
# author:74049
# datetime:2021/3/27 15:46
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

def getfirtwo(key, lis):
    for i in range(len(lis)):
        lis[i] = str(lis[i])
        if len(lis[i]) > 2:
            lis[i] = lis[i][0] + lis[i][1]
    dic = dict(zip(key, lis))
    return dic

if __name__ == '__main__':
    key = [1, 2, 3, 4, 5, 6]
    lis = ['100', 'ssssss', '3333', 22222, 223.2, 2.3006]
    dic = dict(zip(key, lis))
    print("原字典:", dic)
    print("保留值的前两位后:", getfirtwo(key, lis))