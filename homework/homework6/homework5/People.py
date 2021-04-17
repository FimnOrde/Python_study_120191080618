#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:People.py
# author:74049
# datetime:2021/4/17 16:44
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
class People(object):
    attack_value = 0
    health_value = 0
    def __init__(self):
        self.attack_value = 10
        self.health_value = 100
    def attack(self, dog):
        if dog.health_value - self.attack_value >= 0:
            dog.health_value = dog.health_value - self.attack_value
        else:
            dog.health_value = 0