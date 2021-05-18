#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_sqlachemy_bbs.py
@Time    :   2020/05/12 22:48:05
@Author  :   Jackiex 
@Version :   1.0
'''


from models.class22_exercise1 import BBsModel

def test_add():
    # 测试添加,测试添加数据准备
    kwargs = {
        'name': 'Tomcat',
        'id': '888888'
    }

    result_dict = BBsModel.add_bbs(**kwargs)

    if result_dict.get('code') == '200':
        print("插入记录成功")

def test_query():
    # 测试查询，要查询的数据准备
    kwargs = {
        'name': 'TOM',
        'id': '01'
    }

    result_dict = BBsModel.get_bbs(**kwargs)
    print(result_dict)

if __name__ == '__main__':
    # test_add()
    test_query()
