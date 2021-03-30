#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework2.py
# author:74049
# datetime:2021/3/30 15:57
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

if __name__ == '__main__':
    try:
        lis = []
        order = 1
        with open("D:\\PythonTest\\Test\\homework3\\homework1\\input.txt", "r", encoding="utf-8") as file:
            lis = file.readlines()
        for i in lis:
            print(f'#第{order}行', i, end="")
            order = order + 1
    except FileExistsError:
        print("写入的文件不存在")
    except IOError:
        print("写入时发生错误")
    except Exception:
        print("程序发生错误")
