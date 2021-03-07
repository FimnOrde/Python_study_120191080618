#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class2_exercise8.py
# author:74049
# datetime:2021/3/5 13:36
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

'''
#1.测试pythom中变量不需要声明
a = 1.023
b = True
c = 4+5j
d = 'a'
e = "abcds"
f = 203

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
'''

'''
#2.测试多行定义与多行语句
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
total1 = "item_one" + \
        "item_two" + \
        "item_three"
        
print(total)
print(total1)
'''

'''
#3.测试字符串操作
str = 'Runoob'

print(str[0:-2])  # 输出第一个到倒数第三个的所有字符
print(str[3])  # 输出字符串第四个字符
print(str[2:4])  # 输出从第三个开始到第四个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str * 4)  # 输出字符串四次
print(str + 'abcd')  # 连接字符串
print('abcd\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'abcd\nrunoob')  # 在字符串前面添加一个 r，不会发生转义
'''

'''
#4.测试输入，以回车结束
input("输入一个数:")
'''

'''
#5.测试获取本机的最大地址值和运行系统的浮点数各项参数
import sys

print(sys.maxsize)
print(sys.float_info)
'''

'''
#6.测试数据类型比较
a = 123.02

print(isinstance(a,int))
print(isinstance(a,float))
print(isinstance(a,str))
'''

'''
#7.测试比较运算符
print(3>4.22)
print(["abc", "ABC", 100, 200] == ["abc", "ABC", 100, 200])
print(["abc", "ABC", 100, 200] == ["ABC", "abc", 100, 200])
print(["abc", 100, 300] < ["abc", 200, 200])
'''