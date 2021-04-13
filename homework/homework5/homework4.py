#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework4.py
# author:74049
# datetime:2021/4/13 15:28
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework1.py
# author:74049
# datetime:2021/4/13 15:12
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import time

def metric(func):
    def wrapper(*x):
        start_time = time.time()
        f = func(*x)
        end_time = time.time()
        exe_time = end_time - start_time
        print(f'函数{func.__name__}()运行时间:', exe_time)
        return f
    return wrapper

# 无参数无返回值
@metric
def getprimnum1():
    print("20000以内素数:")
    k = 0
    for i in range(2, 20000):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=' ')
            k += 1
            if k == 20:
                k = 0
                print()
    print()

# 有参数
@metric
def getprimnum2(x):
    for i in range(2, 10000):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            x += 1
    print(f'2-10000之间的素数有{x}个')

# 有返回值
@metric
def getprimnum3():
    num = 0
    for i in range(2, 20000):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            num += 1
    return num

# 测试
getprimnum1()
print('-'*30)
getprimnum2(0)
print('-'*30)
print(f'2-20000之内的素数有{getprimnum3()}个')


