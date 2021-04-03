#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework6.py
# author:74049
# datetime:2021/4/3 14:36
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from collections import Counter

def getText():
    try:
        with open("D:\\PythonTest\\Test\\homework3\\homework6\\《老人与海》[英文版].txt", "r", encoding="utf-8") as file:
            txt = file.read()
            txt = txt.lower()
            for i in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~\n':
                txt = txt.replace(i, " ")
            return txt
    except FileExistsError:
        print("写入的文件不存在")
    except IOError:
        print("写入时发生错误")
    except Exception:
        print("程序发生错误")




if __name__ == '__main__':
    txt = getText()
    num = 0
    c = Counter()
    lis = txt.split(" ")
    for i in lis:
        c[i] = c[i] + 1
    try:
        sdic = sorted(c.items(), key=lambda x: x[1], reverse=True)

        dic1 = dict(sdic)
        print("前20出现频率词汇统计:")
        for i in dic1:
            if i != '':
                if num < 20:
                    print(f'{i}:{dic1[i]}')
                num = num + 1
    except Exception:
        print("程序发生错误")


