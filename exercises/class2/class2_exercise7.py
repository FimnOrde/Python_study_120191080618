#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class2_exercise7.py
# author:74049
# datetime:2021/3/5 16:25
# software: PyCharm
'''
this is functiondescription
'''
# import module your need


if __name__ == "__main__":
    std = 'abcdefghijkl'# 定义一个字符串

    print(f'原字符串为:{std}')

    s = input("输入要查找的字符串:")

    # 调用函数查找字符串
    if std.find(s, 0, len(std)) != -1:
        print(f'{s}存在于{std}')
    else:
        print(f'{s}不存在于{std}')

    # 调用函数替换字符串
    s1 = input("输入原字符串要替换的部分:")
    s2 = input("输入替换后新的部分:")

    print(f'新字符串为:{std.replace(s1,s2)}')
    print(f'新字符串长度:{len(std.replace(s1, s2))}')

