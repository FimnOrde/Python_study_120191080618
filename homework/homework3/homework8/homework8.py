#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework8.py
# author:74049
# datetime:2021/4/3 15:11
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import jieba
def statistic(path, num):
    words = []
    with open(path, "r", encoding="utf-8") as file:
        txt = file.read()
        txt = txt.lower()
        for i in '!"#$%&()*+,-./:;<=>?@[\\\']^_{|}~\n':
            txt = txt.replace(i, " ")
        words = jieba.lcut(txt)
        counts = {}
    for word in words:
        if word != " ":
            counts[word] = counts.get(word, 0) + 1

    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    lis = []
    print(f'第{num}篇词频统计:')
    for i in range(10):
        lis.insert(0, items[i])
        word, count = items[i]
        print("{0:<5}:{1:>5}".format(word, count))
    return lis


if __name__ == '__main__':
    path1 = "D:\\PythonTest\\Test\\homework3\\homework8\\1.txt"
    path2 = "D:\\PythonTest\\Test\\homework3\\homework8\\2.txt"
    lis0 = statistic(path1, 1)
    lis1 = statistic(path2, 2)
    num = 0
    for i in lis0:
        for j in lis1:
            if i[0] == j[0]:
                num = num + 1
    print("相似度:", num*10, "%")