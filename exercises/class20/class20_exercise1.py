#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class20_exercise1.py
# author:74049
# datetime:2021/5/14 19:00
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import re


def main():
    tel = input("请输入手机号:")
    # ret = re.match(r"1[35678]\d{9}", tel)
    # 由于手机号位数大于11位也能匹配成功，所以修改如下：
    ret = re.match(r"^1[35678]\d{9}$", tel)
    if ret:
        print("您输入的手机号有效！")
    else:
        print("您输入的是无效的手机号！")


if __name__ == "__main__":
    main()