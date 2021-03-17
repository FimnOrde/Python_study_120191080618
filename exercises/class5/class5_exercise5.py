#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class5_exercise5.py
# author:74049
# datetime:2021/3/17 16:16
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import random
def encapsul0(*orderlis):
    print("封装前:", orderlis)
    return list(orderlis)

def encapsul1(**orderlis):
    return orderlis

if __name__ == '__main__':
    a, b ,c = input("输入三个字符:").split()
    lis = encapsul0(a, b, c)
    print("列表封装后:", lis)

    dic = encapsul1(a=a,b=b, c=c)
    print("字典封装后:", dic)