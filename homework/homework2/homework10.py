#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework10.py
# author:74049
# datetime:2021/3/28 20:04
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def calculate(num1, oper, num2):
    if oper == '+':
        return float(num1) + float(num2)
    elif oper == '-':
        return float(num1) - float(num2)
    elif oper == '*':
        return float(num1) * float(num2)
    elif oper == '/':
        return float(num1) / float(num2)
    else:
        return "输入有误"

if __name__ == '__main__':
    text = input("输入两个数字的算式, 数字与运算符用空格隔开:\n")
    lis = text.split(" ")
    num = calculate(lis[0], lis[1], lis[2])
    print(num)
