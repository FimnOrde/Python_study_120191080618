#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework8.py
# author:74049
# datetime:2021/3/28 19:24
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def most(strin):
    dic = {}
    for i in strin:
        if i != " ":
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] = dic[i] + 1

    sdic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    dic = list(sdic[0])
    return dic[0], dic[1]

if __name__ == '__main__':
    strin = input("请输入一段字符串:")
    char, num = most(strin)
    print("出现最多字符:", char, ":", num)

