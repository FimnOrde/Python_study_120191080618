#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_infomodel1.py
# author:74049
# datetime:2021/5/20 14:48
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import datetime
from homework3.models import infomodel

def test_add(dic):
    # 测试添加,测试添加数据准备
    kwargs = dic

    result_dict = infomodel.BBsModel.add_bbs(**kwargs)

    if result_dict.get('code') == '200':
        print("插入记录成功")
    else:
        print("失败")

def test_query(str):
    # 测试查询，要查询的数据准备
    kwargs = {
        'id': str
    }
    result_dict = infomodel.BBsModel.get_bbs(**kwargs)
    print(result_dict)

def test_dle(str):
    # 测试添加,测试添加数据准备
    kwargs = {
        'id': str
    }

    result_dict = infomodel.BBsModel.dle_bbs(**kwargs)

    if result_dict.get('code') == '200':
        print("删除记录成功")
    else:
        print("失败")

def test_udd(str, dic):
    # 测试添加,测试添加数据准备
    kwargs = {
        'id': str
    }

    result_dict = infomodel.BBsModel.udd_bbs(dic, **kwargs)

    if result_dict.get('code') == '200':
        print("更新记录成功")
    else:
        print("失败")

if __name__ == '__main__':
    print('-' * 5, '插入一条记录', '-' * 5)
    # dic = {
    #     'commentator': 'BOB',
    #     'content':'with',
    #     'isdeleted':0,
    #     'id': '03',
    #     'ctime':datetime.datetime.now()
    # }
    # test_add(dic)

    print('-' * 5, '查询一条记录', '-' * 5)
    # test_query('03')

    print('-' * 5, '更新一条记录', '-' * 5)
    # dic1 = {
    #     'commentator': 'BOBY',
    #     'content': 'with out',
    #     'isdeleted': 0,
    #     'id': '03',
    #     'ctime': datetime.datetime.now()
    # }
    # test_udd('03', dic1)

    print('-' * 5, '删除一条记录', '-' * 5)
    # test_dle('03')