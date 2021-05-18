#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class22_exercise1.py
# author:74049
# datetime:2021/5/18 21:12
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from sqlalchemy import BigInteger, Column, DateTime, String, or_
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base
from . import session

from utils import commons
from utils.response_code import RET

Base = declarative_base()


class BBsModel(Base):
    __tablename__ = 'user_info'

    id = Column(String, primary_key=True)
    name = Column(String(255, 'utf8_general_ci'), info='留言者')


    @classmethod
    def add_bbs(cls, **kwargs):
        try:
            bbs_model = BBsModel(
                name=kwargs.get('name'),
                id=kwargs.get('id')
            )

            session.add(bbs_model)
            session.commit()

        except Exception as e:
            session.rollback()
            return {'code': RET.DBERR, 'message': '数据库异常，更新失败', 'error': str(e)}

        return {'code': RET.OK, 'message': 'OK'}

    @classmethod
    def get_bbs(cls, **kwargs):
        # 获得查询参数
        name = kwargs.get('name')
        id = kwargs.get('id')
        page = int(kwargs.get('page', 1))
        size = int(kwargs.get('size', 10))

        filter_list = []
        # 过滤为空的条件
        if name:
            filter_list.append(cls.name == name)
        if id:
            filter_list.append(cls.id == id)

        # filter_list.append(or_(cls.username == username, cls.content == content))

        try:

            bbs_model = session.query(cls).filter(*filter_list)

            # 计算应该返回的数据
            res = bbs_model.limit(size).offset((page - 1) * size).all()

            if not res:
                return {'code': RET.NODATA, 'message': '无数据', 'error': '无数据'}


            if not res:
                return {'code': RET.NODATA, 'message': '无数据', 'error': '无数据'}
        except Exception as e:
            return {'code': RET.DBERR, 'message': '数据库异常，查询失败', 'error': str(e)}

        return {'code': RET.OK, 'message': 'OK', 'data': commons.all_to_dict(res)}