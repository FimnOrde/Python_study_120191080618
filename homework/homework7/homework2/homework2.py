#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework1.py
# author:74049
# datetime:2021/5/23 21:38
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
homework2 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
    说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
    提示：要用到requests库，BeautifulSoup库
'''
import csv
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from lxml import etree


def get_introduce_url(url):
    print(url)
    word_list = ['企业介绍', '关于我们', '企业发展', '发展历史', '企业概况']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    }
    try:
        response = requests.get(url, headers=headers, timeout=1)
    except:
        return
    soup = BeautifulSoup(response.text, 'lxml')
    html_tree = etree.HTML(response.text)
    a_list = html_tree.xpath('//a')
    for a in a_list:
        try:
            href = a.attrib['href']
        except:
            continue
        href = urljoin(url, href)
        text = ''.join([i.strip() for i in a.xpath('.//text()') if i.strip()]).strip()
        for word in word_list:
            if word in text:
                return href


def main():

    with open('D://PythonTest//Test//homework7//homework2//extracts.txt', 'r', encoding='utf-8') as file:
        url_list = file.readlines()

    n = 0
    for url in url_list:
        try:
            introduce_url = get_introduce_url(url)
        except:
            continue
        if introduce_url:
            if introduce_url.startswith('http'):
                one_data = [url, introduce_url]
                print(one_data)
                f_csv.writerow(one_data)
                result_csv.flush()
                n += 1
                if n == 100:
                    break


if __name__ == '__main__':
    result_csv = open('D://PythonTest//Test//homework7//homework2result.txt', 'w', encoding='utf-8', newline='')
    f_csv = csv.writer(result_csv)
    f_csv.writerow(['首页链接', '企业介绍链接'])
    main()
    result_csv.close()
