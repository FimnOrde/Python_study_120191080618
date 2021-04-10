#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework9.py
# author:74049
# datetime:2021/4/10 16:55
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import requests
import os

url = 'https://img2.baidu.com/it/u=3228549874,2173006364&fm=26&fmt=auto&gp=0.jpg'

dstpath = "D://PythonTest//Test//homework4//homework9//pic.jpg"

try:
    r = requests.get(url)
    with open(dstpath,'wb') as f:
        f.write(r.content)
    print("图片下载成功")

except Exception:
    print("程序出错")