#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class11_exercise2.py
# author:74049
# datetime:2021/4/9 15:54
# software: PyCharm
'''
this is functiondescription
'''
# import module your need


def createCounter():
    global num
    num = 0
    def f():
        global num
        num = num + 1
        def g(num):
            return num
        return g(num)
    return f


if __name__ == '__main__':
    counterA = createCounter()

    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')