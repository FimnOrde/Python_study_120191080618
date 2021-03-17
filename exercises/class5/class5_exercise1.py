#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class5_exercise1.py
# author:74049
# datetime:2021/3/15 13:38
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

def computeprice(weight, price):
    return weight*price

if __name__ == '__main__':
    weight = float(input("输入购买苹果重量:"))
    price = float(input("输入苹果价格:"))
    cost = computeprice(weight, price)
    print('所需支付金额:%.2f'%cost)