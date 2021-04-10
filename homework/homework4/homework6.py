#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework6.py
# author:74049
# datetime:2021/4/10 15:27
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os
import time

def gettime(file_name):

    file_times_modified = time.localtime(os.path.getmtime(file_name))
    year_modified = str(file_times_modified.tm_year)
    month_modified = str(file_times_modified.tm_mon)
    day_modified = str(file_times_modified.tm_mday)

    hour_modified = str(file_times_modified.tm_hour)
    minute_modified = str(file_times_modified.tm_min)
    return year_modified + '-' + month_modified + '-' + day_modified + " " + hour_modified + ':' + minute_modified

def gethrough(srcpath):
    lis = os.listdir(srcpath)
    namelis = []
    timelis = []
    typelis = []
    sizlis = []
    for i in lis:
        name = os.path.join(srcpath, i)
        if os.path.isfile(name):
            namelis.append(i)
            typelis.append(os.path.splitext(i)[1])
            timelis.append(gettime(name))
            sizlis.append(str(os.path.getsize(name)) + "b")

        elif os.path.isdir(name):
            namelis.append(i)
            typelis.append("文件夹")
            timelis.append(gettime(name))
            sizlis.append("")
    return namelis, timelis, typelis, sizlis


if __name__ == '__main__':
    srcpath = "D:\\PythonTest\\Test\\homework4"

    namelis, timelis, typelis, sizlis = gethrough(srcpath)
    num = len(namelis)
    print("{:" "<18}".format("名称"), end=" ")
    print("{:" "<18}".format("修改日期"), end=" ")
    print("{:" "<9}".format("类型"), end=" ")
    print("{:" "<10}".format("大小"))
    for i in range(num):
        print("{:" "<20}".format(namelis[i]),end=" ")
        print("{:" "<20}".format(timelis[i]), end=" ")
        print("{:" "<10}".format(typelis[i]),end=" ")
        print("{:" "<10}".format(sizlis[i]))
