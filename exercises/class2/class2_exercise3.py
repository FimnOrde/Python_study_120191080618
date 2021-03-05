#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class2_exercise3.py
# author:74049
# datetime:2021/3/4 13:20
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 通过字符串切片方式反向输出
def reverseWords(input):
    # 翻转字符串
    output = input[-1::-1]

    return output

# 存放到列表中，然后反向输出
def reverseWords1(input):
    # 将传入的字符串转化为为列表
    list1 = list(input)

    # 翻转列表
    inputWords = list1[-1::-1]

    # 重新组合字符串
    output = ''.join(inputWords)

    return output


if __name__ == "__main__":
    string = input("输入一个字符串:")

    rw = reverseWords(string)
    rw1 = reverseWords1(string)

    print("第一种方式:"+rw)
    print("第二种方式:"+rw)
