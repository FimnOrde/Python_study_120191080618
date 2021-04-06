#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework3.py
# author:74049
# datetime:2021/4/6 14:45
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import base64

lis = []
print("输入五个同学的姓名, 账号, 密码(用空格隔开):")
for i in range(5):
    info = input().split(" ")
    lis0 = list(info)
    lis.append(lis0)

for i in lis:
    element =bytes(i[2], encoding='utf-8')
    i[2] = base64.b64encode(element)

try:
    with open("D:\\PythonTest\\Test\\homework4\\homework3\\account.txt", "w", encoding="utf-8") as file:
        for i in lis:
            for j in i:
                file.write(str(j))
                file.write(" ")
            file.write("\n")
    print("写入成功")
except Exception:
    print("文件写入出错")

# Tom admin 12345
# JERRY root 23654
# BOB fooil 58941
# JESS yuio 985612
# MARY makil 451278