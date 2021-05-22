#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:infomodel.py
# author:74049
# datetime:2021/5/20 14:43
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import math

from sqlalchemy import BigInteger, Column, DateTime, String, and_, Integer
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base
from . import session
from . import stu_infomodel
from . import class_infomodel

from ..utils import commons
from ..utils.response_code import RET

Base = declarative_base()


class BBsModel(Base):
    __tablename__ = 'stu_info'

    num = Column(Integer, primary_key=True)
    gender = Column(String(255, 'utf8_general_ci'), info='性别')
    name = Column(String(255, 'utf8_general_ci'), info='姓名')
    age = Column(Integer,  info='年龄')
    isdeleted  = Column(Integer,  info='是否删除')


    @classmethod
    def get_bbs(cls, **kwargs):
        # 获得查询参数
        name = kwargs.get('name')
        num = kwargs.get('num')
        gender = kwargs.get('gender')
        age = kwargs.get('age')
        isdeleted = kwargs.get('isdeleted')
        page = int(kwargs.get('page', 1))
        size = int(kwargs.get('size', 10))

        filter_list = []
        # 过滤为空的条件
        if num != (None,):
            filter_list.append(cls.num == num)
        elif gender != (None,):
            filter_list.append(cls.gender == gender)
        elif name != (None,):
            filter_list.append(name in cls.name)

        try:
            bbs_model = session.query(cls).filter(*filter_list)

            # 计算应该返回的数据
            res = bbs_model.limit(size).offset((page - 1) * size).all()

            if not res:
                print("数据库中不存在此id的记录")
                return {'code': RET.NODATA, 'message': '无数据', 'error': '无数据'}


        except Exception as e:
            print("数据库表格读取错误")
            return {'code': RET.DBERR, 'message': '数据库异常，查询失败', 'error': str(e)}

        return {'code': RET.OK, 'message': 'OK', 'data': commons.all_to_dict(res)}

    @classmethod
    def get_all_student(cls, **kwargs):
        page = int(kwargs.get('page', 1))
        size = int(kwargs.get('size', 20))
        try:
            students = session.query(cls)
            count = students.count()
            pages = math.ceil(count / size)
            students = students.limit(size).offset((page - 1) * size).all()

            if not students:
                return {'code': RET.NODATA, 'message': '没有学生信息', 'error': '没有学生信息'}

            # 处理返回的数据
            res = commons.all_to_dict(students)

            return {'code': RET.OK, 'message': 'OK', 'pages': pages, 'data': res}

        except Exception as e:
            return {'code': RET.DBERR, 'message': '数据库异常，获取学生信息失败', 'error': str(e)}

    @classmethod
    def two_table_search(cls, **kwargs):
        """
        两个表联合查询--获取学生完整信息（学生信息和班级名称）的查询；分页显示
        """
        page = int(kwargs.get('page', 1))
        size = int(kwargs.get('size', 20))

        try:
            students = session.query(cls.name,
                                     cls.num,
                                     cls.age,
                                     cls.gender,
                                     cls.isdeleted,
                                     class_infomodel.StudentGroup.clas
                                     ). \
                outerjoin(class_infomodel.StudentGroup, and_(stu_infomodel.StudentGroup.num == class_infomodel.StudentGroup.num))


            count = students.count()
            pages = math.ceil(count / size)

            students = students.limit(size).offset((page - 1) * size).all()


            if not students:
                return {'code': RET.NODATA, 'message': '没有学生信息', 'error': '没有学生信息'}

            # 处理返回的数据
            # res = commons.all_to_dict(students)



            return {'code': RET.OK, 'message': 'OK', 'pages': pages, 'data': students}

        except Exception as e:
            return {'code': RET.DBERR, 'message': '数据库异常，获取学生信息失败', 'error': str(e)}

