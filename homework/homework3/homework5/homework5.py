#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework5.py
# author:74049
# datetime:2021/3/30 17:04
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
try:
    lis = []
    with open("D:\\PythonTest\\Test\\homework3\\homework5\\Blowing in the wind.txt", "r", encoding="utf-8") as file:
        lis = file.readlines()

    lis.insert(0, "Blowin' in the wind\n")
    lis.insert(1, "Bob Dylan\n")
    lis.insert(len(lis), "1962 by Warner Bros.Inc")

    with open("D:\\PythonTest\\Test\\homework3\\homework5\\Blowing in the wind.txt", "w", encoding="utf-8") as file:
        file.writelines(lis)

    for i in lis:
        print(i, end="")

except FileExistsError:
        print("写入的文件不存在")
except IOError:
        print("写入时发生错误")
except Exception:
    print("程序发生错误")

