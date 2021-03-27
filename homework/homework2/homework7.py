#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework7.py
# author:74049
# datetime:2021/3/27 15:57
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import random

def marks(dic):
    for i in dic.keys():
        if dic[i] >= 90:
            print(f'{i}同学成绩等级为A')
        elif dic[i] >= 80:
            print(f'{i}同学成绩等级为B')
        elif dic[i] >= 70:
            print(f'{i}同学成绩等级为C')
        else:
            print(f'{i}同学成绩等级为D')


if __name__ == '__main__':
    # 同学名称
    lis_key = [i + 1 for i in range(20)]
    # 同学成绩
    lis_value = [random.randint(50, 100) for i in range(20)]
    # 生成字典
    dic = dict(zip(lis_key, lis_value))

    print("学生成绩为:")
    for i in dic.items():
        print(i, end=" ")
    print()

    print("学生成绩等级为:")
    marks(dic)