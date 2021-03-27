#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework4.py
# author:74049
# datetime:2021/3/27 15:26
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

def statistic(strin):
    alp = 0
    num = 0
    spa = 0
    oth = 0
    for i in strin:
        if i.isdigit():
            num = num +1
        elif i.isalpha():
            alp = alp + 1
        elif i.isspace():
            spa = spa + 1
        else:
            oth = oth + 1
    return num, alp, spa, oth

if __name__ == '__main__':
    text = input("请输入一段字符串:")
    num, alp, spa, oth = statistic(text)
    print(f'数字有{num}个')
    print(f'字母有{alp}个')
    print(f'空格有{spa}个')
    print(f'其他有{oth}个')
