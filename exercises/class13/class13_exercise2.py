#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class13_exercise2.py
# author:74049
# datetime:2021/4/16 15:48
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value < 0:
            raise ValueError('width must > 0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        if value < 0:
            raise ValueError('height must > 0')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print("分辨率为:", s.resolution)