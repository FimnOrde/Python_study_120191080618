#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class4_exercise2.py
# author:74049
# datetime:2021/3/13 14:44
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

dict0 = {"name": "TOM", "ID": "0100", "class": "1902", "age": 18}

# 增加元素
dict0["faculty"] = "Programming"
print(dict0)

# 修改元素
dict0["age"] = 20
print(dict0)

# 删除元素
# del dict0["age"]
dict0.pop("age")
print(dict0)

# 清空字典
dict0.clear()
print(dict0)