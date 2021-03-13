#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class4_exercise3.py
# author:74049
# datetime:2021/3/13 14:52
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

values = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

# 两种方法初始化
set0 = {'apple', 'orange', 'pineapple'}
set1 = set(values)

print(f'集合1:{set0}')
print(f'集合2:{set1}')

# 添加元素
set1.update(['papaya', 'plum'])
print(f'集合2添加元素后:{set1}')

# 删除元素
set1.discard('apple')
print(f'集合2删除元素后:{set1}')

# 集合运算
print(f'两集合交集:{set0 & set1}')
print(f'两集合并集:{set0 | set1}')
print(f'两集合差集:{set0 - set1}')
print(f'两集合补集:{set0 ^ set1}')

