#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class5_exercise2.py
# author:74049
# datetime:2021/3/15 14:20
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def listope(lis):
    for i in lis:
        print(i, end=" ")
    print('\n', '-'*20)
    lis.append([1, 2, 3, 4])
    for i in lis:
        print(i, end=" ")

if __name__ == '__main__':
    lis = [5, 6, 7, 8]
    print("传参前地址:", id(lis))
    listope(lis)
    print("\n传参后地址:", id(lis))
