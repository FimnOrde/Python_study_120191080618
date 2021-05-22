#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework4.py
# author:74049
# datetime:2021/5/22 14:32
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import json

datas = [
    {
        "name":"Frank",
        "age":15,
        "genda":"男"
    },
    {
        "name":"tracy",
        "age":20,
         "genda":"女"
    },
    {
        "name":"cythia",
        "age":21,
         "genda":"女"
    },
    {
        "name":"王五",
        "age":19,
       "genda":"男"
    },
    {
        "name":"jackie",
        "age":19,
       "genda":"男"
    }
]


print('-'*5, '打印输出年龄大于20的人员', '-'*5)
for i in datas:
    if i['age'] > 20:
        print(f'姓名:{i["name"]}, 性别:{i["genda"]}, 年龄:{i["age"]}')
print()


print('-'*5, '向列表中新增数据', '-'*5)
data = {
    "name":"Jessy",
    "age":23,
    "genda":"女"
    }
datas.append(data)
for i in datas:
    print(f'姓名:{i["name"]}, 性别:{i["genda"]}, 年龄:{i["age"]}')
print()


print('-'*5, '向列表中新增数据', '-'*5)
num_male = 0
num_female = 0
for i in datas:
    if i['genda'] == '男':
        num_male += 1
    if i['genda'] == '女':
        num_female += 1
print('男生人数:', num_male)
print('女生人数:', num_female)