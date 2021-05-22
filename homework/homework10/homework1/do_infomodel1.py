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
from homework1.models import infomodel
from sqlalchemy import and_, or_
from homework1.models import session
from utils import commons
from homework1.models import class_infomodel
from homework1 import assort


def test_query(kwargs):
    # 测试查询，要查询的数据准备
    result_dict = infomodel.BBsModel.get_bbs(**kwargs)
    return result_dict

def query_condition_opa():
    datas = commons.all_to_dict(session.query(infomodel.BBsModel).filter(infomodel.BBsModel.name.like("黄%")).all())
    lis = []
    for i in datas:
        if len(i['name']) == 2:
            lis.append(i)
    return lis

def query_condition_notdel():
    return commons.all_to_dict(session.query(infomodel.BBsModel).filter(infomodel.BBsModel.isdeleted == 0).all())


def query_condition_acc(num):
    datas = []
    for i in num:
        datas.append(commons.all_to_dict(session.query(infomodel.BBsModel).filter(infomodel.BBsModel.num == i).all()))
    return datas

def query_condition_acc1(num):
    datas = []
    for i in num:
        datas.append(commons.all_to_dict(session.query(class_infomodel.StudentGroup).filter(class_infomodel.StudentGroup.num == i).all()))
    return datas

def query_condition_gen(gender):
    return commons.all_to_dict(session.query(infomodel.BBsModel).filter(infomodel.BBsModel.gender == gender).all())

if __name__ == '__main__':

    print('-'*10, '查询所有男生姓名,年龄,班级','-'*10)
    # res1 = infomodel.BBsModel.two_table_search()['data']
    # lis = []
    # for i in res1:
    #     if i[3] == '男':
    #         lis.append(i)
    # for i in lis:
    #     print(f'编号:{i[1]}, 姓名:{i[0]}, 性别:{i[3]}, 年龄:{i[2]}, 是否删除:{i[4]}, 班级:{i[5]}')


    print('-' * 10, '查询编号小于4或没被删除的学生', '-' * 10)
    # res2_1 = query_condition_acc([1, 2, 3, 4])
    # res2_2 = query_condition_notdel()
    # for i in res2_1:
    #     if i[0] not in res2_2:
    #         res2_2.append(i[0])
    # lis = sorted(res2_2, key=lambda x: int(x['num']), reverse=False)
    # for i in lis:
    #     print(f'编号:{i["num"]}, 姓名:{i["name"]}, 性别:{i["gender"]}, 年龄:{i["age"]}, 是否删除:{i["isdeleted"]}')


    print('-'*10, '查询姓黄且名是一个字的学生','-'*10)
    # res3 = query_condition_opa()
    # for i in res3:
    #      print(f'编号:{i["num"]}, 姓名:{i["name"]}, 性别:{i["gender"]}, 年龄:{i["age"]}, 是否删除:{i["isdeleted"]}')

    print('-' * 10, '查询编号是1,3,8的学生', '-' * 10)
    # res4 = query_condition_acc([1, 3, 8])
    # for i in res4:
    #     print(f'编号:{i[0]["num"]}, 姓名:{i[0]["name"]}, 性别:{i[0]["gender"]}, 年龄:{i[0]["age"]}, 是否删除:{i[0]["isdeleted"]}')

    print('-' * 10, '查询编号是3至8的学生', '-' * 10)
    # lis = []
    # for i in range(3, 9):
    #     lis.append(i)
    # res5 = query_condition_acc(lis)
    # for i in res5:
    #     print(f'编号:{i[0]["num"]}, 姓名:{i[0]["name"]}, 性别:{i[0]["gender"]}, 年龄:{i[0]["age"]}, 是否删除:{i[0]["isdeleted"]}')

    print('-' * 10, '查询未删除男生信息,按年龄降序', '-' * 10)
    # res6_1 = query_condition_gen('男')
    # res6_2 = query_condition_notdel()
    # for i in res6_1:
    #     if i not in res6_2:
    #         res6_1.remove(i)
    # lis = sorted(res6_1, key=lambda x: x['age'], reverse=True)
    # for i in lis:
    #     print(f'编号:{i["num"]}, 姓名:{i["name"]}, 性别:{i["gender"]}, 年龄:{i["age"]}')

    print('-' * 10, '查询女士总数', '-' * 10)
    # res7 = query_condition_gen('女')
    # print('女生总数是:', len(res7))

    print('-'*10, '查询所学生平均年龄','-'*10)
    # avg_age = 0
    # num = 0
    # res8 = infomodel.BBsModel.get_all_student()['data']
    # for i in res8:
    #     num += 1
    #     avg_age += int(i['age'])
    # print('所有学生平均年龄为:', '%.2f' % (avg_age/num))


    print('-' * 10, '分别统计男/女的平均年龄', '-' * 10)
    # avg_age, avg_age1 = 0, 0
    # num, num1 = 0, 0
    # res9_male = query_condition_gen('男')
    # print('1.男生数据')
    # for i in res9_male:
    #     print(f'编号:{i["num"]}, 姓名:{i["name"]}, 性别:{i["gender"]}, 年龄:{i["age"]}')
    #     num += 1
    #     avg_age += int(i['age'])
    # print('所有男生平均年龄为:', '%.2f' % (avg_age / num))
    #
    # res9_female = query_condition_gen('女')
    # print('1.女生数据')
    # for i in res9_female:
    #     print(f'编号:{i["num"]}, 姓名:{i["name"]}, 性别:{i["gender"]}, 年龄:{i["age"]}')
    #     num1 += 1
    #     avg_age1 += int(i['age'])
    # print('所有女生平均年龄为:', '%.2f' % (avg_age1 / num1))

    print('-' * 10, '按照性别分组', '-' * 10)
    # lis1 = query_condition_gen('男')
    # lis2 = query_condition_gen('女')
    # lis3 = query_condition_gen('中性')
    # lis4 = query_condition_gen('保密')
    # assort.assort(lis1, lis2, lis3, lis4)















