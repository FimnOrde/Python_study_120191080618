#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework8.py
# author:74049
# datetime:2021/3/14 15:09
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from operator import itemgetter

info1 = [("工号", 11), ("姓名", "AA"), ("工龄", 5), ("工资", 3000)]
info2 = [("工号", 12), ("姓名", "BB"), ("工龄", 2), ("工资", 2000)]
info3 = [("工号", 13), ("姓名", "CC"), ("工龄", 4), ("工资", 2500)]
info4 = [("工号", 14), ("姓名", "DD"), ("工龄", 70), ("工资", 5000)]
info5 = [("工号", 15), ("姓名", "EE"), ("工龄", 3), ("工资", 3000)]
info6 = [("工号", 16), ("姓名", "FF"), ("工龄", 9), ("工资",6000)]
info7 = [("工号", 17), ("姓名", "GG"), ("工龄", 11), ("工资", 7000)]
info8 = [("工号", 18), ("姓名", "HH"), ("工龄", 2), ("工资", 2000)]
info9 = [("工号", 19), ("姓名", "II"), ("工龄", 1), ("工资", 1500)]
info10 = [("工号", 20), ("姓名", "JJ"), ("工龄", 6), ("工资", 5000)]

dic1 = dict(info1)
dic2 = dict(info2)
dic3 = dict(info3)
dic4 = dict(info4)
dic5 = dict(info5)
dic6 = dict(info6)
dic7 = dict(info7)
dic8 = dict(info8)
dic9 = dict(info9)
dic10 = dict(info10)

dic = [dic1, dic2, dic3, dic4, dic5, dic6, dic7, dic8, dic9, dic10]

sdic = sorted(dic, key = itemgetter("工资"))
sdic.reverse()

print("按工资高低排序:")
for i in sdic:
    print(i)
