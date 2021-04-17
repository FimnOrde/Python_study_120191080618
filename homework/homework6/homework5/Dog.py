#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:Dog.py
# author:74049
# datetime:2021/4/17 16:43
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
class Dog(object):
    attack_value = 0
    health_value = 0
    def __init__(self):
        self.attack_value = 15
        self.health_value = 80
    def attack(self, people):
        if people.health_value - self.attack_value >= 0:
            people.health_value = people.health_value - self.attack_value
        else:
            people.health_value = 0

