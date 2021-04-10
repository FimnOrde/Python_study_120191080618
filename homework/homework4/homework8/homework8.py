#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework8.py
# author:74049
# datetime:2021/4/10 16:26
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import random

lis = []
for i in range(1200):
    lastip = random.randint(1, 254)
    lis.append(f'170.25.254.{str(lastip)}')

with open("D:\\PythonTest\\Test\\homework4\\homework8\\ip.txt", "w", encoding='utf-8')as file:
    for i in lis:
        file.write(i)
        file.write('\n')
    print("写入成功")
keys = []
values = []

for i in lis:
    if i not in keys:
        keys.append(i)
        values.append(lis.count(i))
    else:
        continue
tup = zip(keys, values)
dic = dict(tup)

sdic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print("ip.txt文件中出现频率前十 的ip是:")
for i in range(10):
    print(f'{sdic[i][0]}:{sdic[i][1]}')



