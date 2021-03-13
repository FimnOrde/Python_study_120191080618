#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class4_exercise1.py
# author:74049
# datetime:2021/3/11 13:52
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

dict0 = {"name": "TOM", "ID": "0100", "class": "1902", "age": 18}
dict1 = {"name": "HANG", "ID": "0101"}
dict2 = {"name": "JESS", "ID": "0102"}
dict3 = {"name": "BOB", "ID": "0103"}
dict4 = {"name": "ALLEN", "ID": "0104"}
dict5 = {"name": "RAB", "ID": "0105"}
dict6 = {"class1": dict1, "class2": dict2,
         "class3": dict3, "class4": dict4, "class5": dict5}

# 整体输出
print(dict0)

# 通过键来访问
for i in dict6:
    for j in dict6[i]:
        print(f"{j}:{dict6[i][j]}", end=" ")
    print(end="\n")
