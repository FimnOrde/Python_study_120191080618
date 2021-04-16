#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework4.py
# author:74049
# datetime:2021/4/16 16:46
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
class Student(object):
    __name = ''
    __age = 0
    __sex = ''
    __score1, __score2, __score3 = 0, 0, 0
    def __init__(self, name, age, sex, score1, score2, score3):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__score1 = score1
        self.__score2 = score2
        self.__score3 = score3

    def get_personinfo(self):
        return self.__name, self.__age, self.__sex

    def get_courceinfo(self):
        sum = self.__score1 + self.__score2 + self.__score3
        ave = "{:.2f}".format(sum / 3)

        return self.__score1, self.__score2, self.__score3, sum, ave

s1 = Student("TOM", 19, "male", 98, 87, 86)
s2 = Student("BOB", 20, "female", 76, 77, 89)
print("姓名   年龄  性别   语文   数学   英语   总分   平均分")
for i in s1.get_personinfo():
    print(i, end="   ")
for i in s1.get_courceinfo():
    print(i, end="    ")

print()

for i in s2.get_personinfo():
    print(i, end="   ")
for i in s2.get_courceinfo():
    print(i, end="    ")