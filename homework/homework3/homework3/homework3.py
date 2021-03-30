#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework3.py
# author:74049
# datetime:2021/3/30 16:08
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

if __name__ == '__main__':
    try:
        lis = []
        with open("D:\\PythonTest\\Test\\homework3\\homework3\\grade.txt", "r", encoding="utf-8") as file:
            lis = file.readlines()

        lis0 = lis[1:]
        lis1 = [int(i[-3]+i[-2]) for i in lis0]

        dic = dict(zip(lis1, lis0))
        dic_sorted = sorted(dic.items(), key = lambda x:x[0], reverse=True)

        print("成绩排序后:")
        for i in dic_sorted:
            print(i[1], end="")


    except FileExistsError:
        print("写入的文件不存在")
    except IOError:
        print("写入时发生错误")
    except Exception:
        print("程序发生错误")
