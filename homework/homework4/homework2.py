#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework2.py
# author:74049
# datetime:2021/4/6 14:23
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from datetime import date
try:
    year, month, day = input("输入日期（用空格间隔）:").split(" ")

    week = date(int(year), int(month), int(day)).isocalendar()
    weekday = date(int(year), int(month), int(day)).weekday()+1

    print(f'这天是当年第{week[1]}周')
    print(f'这天是星期{weekday}')

    print("-"*30)

    month, day = input("输入日期（月, 日）查询校历周数:").split(" ")
    week = date(2020, int(month), int(day)).isocalendar()
    print(f'这天校历是第{week[1]-7}周')
except Exception:
    print("程序出错")