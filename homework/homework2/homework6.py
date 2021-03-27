#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework6.py
# author:74049
# datetime:2021/3/27 15:46
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def fib(n):
    fir = 0
    sec = 1

    while True:

        i = sec + fir
        if i > n:
            break
        fir = sec
        sec = i

        print(i, end=" ")

if __name__ == '__main__':
    n = float(input("输入一个数, 使得斐波那契数列最大值不大于这个数:"))
    print("数列为:", end="")
    fib(n)