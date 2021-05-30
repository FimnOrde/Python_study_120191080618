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
from database_oper.models import infomodel
from database_oper.utils import commons
from database_oper.models import session

def test_add(content, num):
    # 测试添加,测试添加数据准备
    num += 1
    dic = {
        'content':'{s}'.format(s=content),
        'num':str(num),
        'state': 'Undo',
        'time':datetime.datetime.now()
    }
    kwargs = dic

    result_dict = infomodel.BBsModel.add_bbs(**kwargs)

def test_query(str):
    # 测试查询，要查询的数据准备
    kwargs = {
        'id': str
    }
    result_dict = infomodel.BBsModel.get_bbs(**kwargs)
    print(result_dict['data'])

def test_dle(str):
    # 测试添加,测试添加数据准备
    kwargs = {
        'num': str
    }

    result_dict = infomodel.BBsModel.dle_bbs(**kwargs)

    if result_dict.get('code') == '200':
        pass
    else:
        print("失败")

def test_udd(str, info):
    # 测试添加,测试添加数据准备
    kwargs = {
        'num': str,
        'info':info
    }

    result_dict = infomodel.BBsModel.udd_bbs(**kwargs)

    if result_dict.get('code') == '200':
        pass
    else:
        print("失败")

def query_condition_opa(str):
    s = '%{s}%'.format(s=str)
    datas = commons.all_to_dict(session.query(infomodel.BBsModel).filter(infomodel.BBsModel.content.like(s)).all())
    return datas

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
    query_condition_opa('cal')

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

