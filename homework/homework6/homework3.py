#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework3.py
# author:74049
# datetime:2021/4/16 16:20
# software: PyCharm
'''
this is functiondescription
'''
#import module your need
class Dictclass(object):
    object = {}
    def __init__(self, object):
        self.object = object

    def del_key(self, key):
        if key in self.object.keys():
            del self.object[key]
            return self.object
        else:
            return "not found"

    def get_dict(self, key):
        if key in self.object.keys():
            return self.object[key]
        else:
            return "not found"

    def get_key(self):
        lis = []
        for i in self.object.keys():
            lis.append(i)
        return lis

    def update_dict(self, dic):
        self.object.update(dic)
        return self.object






dic = {'name':"牧羊犬", "colour":"白色", "num":23, "price":2000}
dic1 = {"date":"2021.4.16", "payment":"installment"}
opedic = Dictclass(dic)

print("删除key=num:", opedic.del_key("num"))
print("判断key=num是否在字典中:", opedic.get_dict("num"))
print("字典的键组成的列表:", opedic.get_key())
print("两个字典合并:", opedic.update_dict(dic1))