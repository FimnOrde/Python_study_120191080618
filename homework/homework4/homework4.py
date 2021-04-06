#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework4.py
# author:74049
# datetime:2021/4/6 15:14
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import base64

try:
    with open("D:\\PythonTest\\Test\\homework4\\homework3\\account.txt", "r", encoding="utf-8") as file:
        midlis = file.readlines()

    flag = 0
    flag1 = 0
    lis = []
    for i in midlis:
        info = i.split(" ")
        lis.append(info)

    name = input("输入登录同学姓名:")

    num = 0
    for i in lis:
        if name == i[0]:
            account = input("请输入账号:")
            flag = 1
            break
        num = num +1
    else:
        print("不存在此用户")

    if flag == 1:
        if account == lis[num][1]:
            password = input("请输入密码:")
            flag1 = 1
        else:
            print("账号输入错误")

    if flag1 == 1:
        word = base64.b64decode(lis[num][2][2:-2]).decode()
        if password == word:
            print("登陆成功")
        else:
            print("密码错误, 登录失败")

except Exception:
    print("程序出错")