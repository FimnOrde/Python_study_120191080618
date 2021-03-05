#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class2_exercise6.py
# author:74049
# datetime:2021/3/5 16:18
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

if __name__ == "__main__":
    #练习f-string
    movie = '流浪地球'
    ticket = 45.9
    count = 15
    total = ticket * count

    print(f'电影:{movie}')
    print(f'人数:{count}')
    print(f'单价:{ticket}')
    print(f'总票价:{total}')

