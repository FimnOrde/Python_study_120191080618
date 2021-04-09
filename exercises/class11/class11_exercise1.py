#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class11_exercise1.py
# author:74049
# datetime:2021/4/8 14:55
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

def calculate(x, y, operator, f):
    return f(x, y, operator)

def operat(x, y, operator):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        if y != 0:
            return x / y
        else:
            return "除数不能为0"
    else:
        return "算式有错"


if __name__ == '__main__':
    print(calculate(23.03, 56.17, '+', operat))
    print(calculate(23.03, 56.17, '-', operat))
    print(calculate(23.03, 56.17, '*', operat))
    print(calculate(23.03, 56.17, '/', operat))
    print(calculate(23.03, 0, '/', operat))
    print(calculate(23.03, 56.17, '?', operat))
