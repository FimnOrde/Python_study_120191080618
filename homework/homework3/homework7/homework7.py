#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework7.py
# author:74049
# datetime:2021/4/3 16:32
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
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
def statistic(path):
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
    print("文章词频统计:")
    for i in range(10):
        lis.insert(0, items[i])
        word, count = items[i]
        print("{0:<5}:{1:>5}".format(word, count))
    return lis


if __name__ == '__main__':
    path = "D:\\PythonTest\\Test\\homework3\\homework7\\text.txt"
    statistic(path)

