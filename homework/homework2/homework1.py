#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework1.py
# author:74049
# datetime:2021/3/27 15:27
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

def counter(seq):
    print(type(seq), end=" ")
    num = len(seq)
    return num

if __name__ == '__main__':
    lis = [1, 2, 2.3, "s", 5.2]
    tup = (1, 2, 2.3, 5.2, "df", "sd", 1, 65)
    dic = {1:"a", 2:"b", 3:"c"}
    print("对象长度为:", counter(lis))
    print("对象长度为:", counter(tup))
    print("对象长度为:", counter(dic))