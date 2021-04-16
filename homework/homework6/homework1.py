#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework1.py
# author:74049
# datetime:2021/4/16 16:02
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
class Dog(object):
    dic1 = {'name':"牧羊犬", "colour":"白色", "num":23, "price":2000}
    dic2 = {'name': "哈士奇", "colour": "黑色", "num":41, "price":1575}
    dic3 = {'name': "田园犬", "colour": "黄色", "num":36, "price":800}
    dognum = [dic1["num"], dic2["num"], dic3["num"]]
    lis = [dic1, dic2, dic3]
    name = ''
    num = 0
    def __init__(self, name, num):
        self.name = name
        self.num = num
    def transaction(self):
        order = 0
        for i in self.lis:
            if self.name in i.values():
                if Dog.dognum[order] >= self.num:
                    print(f'购买{i["name"]}{self.num}只')
                    Dog.dognum[order] = Dog.dognum[order] - self.num
                    return ""


                elif 0 < Dog.dognum[order] < self.num:
                    print(f'最多购买{i["name"]}{i["num"]}只')
                    Dog.dognum[order] = 0
                    return ""

                else:
                    return "这种狗已卖光"
                order = order + 1
            else:
                order = order + 1
                continue

        return "商店内没有这种狗"



d1 = Dog("哈士奇", 47)
d2 = Dog("牧羊犬", 2)
d3 = Dog("牧羊犬", 8)
d4 = Dog("田园犬", 18)
print(d1.transaction())
print(d2.transaction())
print(d3.transaction())
print(d4.transaction())
print("-"*50)
print("牧羊犬还有:", Dog.dognum[0])
print("哈士奇还有:", Dog.dognum[1])
print("田园犬还有:", Dog.dognum[2])