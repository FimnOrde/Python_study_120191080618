#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework2.py
# author:74049
# datetime:2021/4/16 16:07
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
class Student(object):
    __name = ''
    __age = 0
    __score1, __score2, __score3 = 0, 0, 0
    def __init__(self, name, age, score1, score2, score3):
        self.__name = name
        self.__age = age
        self.__score1 = score1
        self.__score2 = score2
        self.__score3 = score3
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_cource(self):
        if self.__score1 > self.__score2:
            max = self.__score1
            if max > self.__score3:
                return max
            else:
                return self.__score3
        else:
            max = self.__score2
            if max > self.__score3:
                return max
            else:
                return self.__score3


s1 = Student("TOM", 19, 98, 87, 86)
s2 = Student("BOB", 20, 76, 77, 89)

print("姓名:", s1.get_name())
print("年龄:", s1.get_age())
print("最高分:", s1.get_cource())

print("姓名:", s2.get_name())
print("年龄:", s2.get_age())
print("最高分:", s2.get_cource())