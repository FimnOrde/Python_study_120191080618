#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework2.py
# author:74049
# datetime:2021/5/6 21:49
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import requests
from concurrent.futures import ThreadPoolExecutor
import threading
import datetime
mutex = threading.Lock()

def getHtmlText(url):
    try:

        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(url + "可以访问")

    except:
        print(url + "产生异常")

if __name__ == '__main__':
    urls = []
    with open("D:\\PythonTest\\Test\\homework8\\homework2\\url_data.txt", 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line:
                urls.append(line)
            else:
                break

    with ThreadPoolExecutor(max_workers=10) as t:
        time1 = datetime.datetime.now()
        for url in urls:
            url = url.strip('\n')
            task1 = t.submit(getHtmlText, url)
        time2 = datetime.datetime.now()
        exet1 = time2 - time1




