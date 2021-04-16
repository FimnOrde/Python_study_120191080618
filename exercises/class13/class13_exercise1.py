#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class13_exercise1.py
# author:74049
# datetime:2021/4/16 15:27
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

class Dog:
    colour = ''
    name = ''
    num = 0
    def __init__(self, colour, name):
        self.colour = colour
        self.name = name
        Dog.num += 1

    def bark(self):
        print(f'{self.name}在叫')

dog1 = Dog('黄色', '阿拉斯加犬')
dog2 = Dog('白色', '田园犬')
dog3 = Dog('黑色', '雪橇犬')
dog4 = Dog('灰色', '牧羊犬')
dog1.bark()
dog2.bark()
dog3.bark()
dog4.bark()

print("实例化对象个数:", Dog.num)