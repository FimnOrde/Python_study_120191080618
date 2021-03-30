#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework1.py
# author:74049
# datetime:2021/3/30 15:40
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

def inputtext():
    lis = []
    print("输入多行文字, 按回车提行, 以空行为结尾:")
    while True:
        text = input()
        if not text:
            return lis
        lis.append((text))

if __name__ == '__main__':
    try:
        lis = inputtext()
        with open("D:\\PythonTest\\Test\\homework3\\homework1\\input.txt", "w", encoding="utf-8") as file:
            for i in lis:
                file.write(i)
                file.write("\n")
        print("写入成功")
    except FileExistsError:
        print("写入的文件不存在")
    except IOError:
        print("写入时发生错误")
    except Exception:
        print("程序发生错误")