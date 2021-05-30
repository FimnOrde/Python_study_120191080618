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
from sqlalchemy import BigInteger, Column, DateTime, String, or_, Integer
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base
from . import session

from ..utils import commons
from ..utils.response_code import RET

Base = declarative_base()


class BBsModel(Base):
    __tablename__ = 'todolist'

    num = Column(String, primary_key=True)
    content = Column(String(255, 'utf8_general_ci'), info='事务信息')
    time = Column(DateTime, server_default=FetchedValue(),primary_key=True)
    state = Column(Integer,  info=0)

    @classmethod
    def add_bbs(cls, **kwargs):
        try:
            bbs_model = BBsModel(
                content=kwargs.get('content'),
                time=kwargs.get('time'),
                state = kwargs.get('state'),
                num = kwargs.get('num')
            )

            session.add(bbs_model)
            session.commit()

        except Exception as e:
            session.rollback()
            print("数据库表格读取错误")
            return {'code': RET.DBERR, 'message': '数据库异常，更新失败', 'error': str(e)}

        return {'code': RET.OK, 'message': 'OK'}

    @classmethod
    def get_bbs(cls, **kwargs):
        # 获得查询参数
        num = kwargs.get('id')
        page = int(kwargs.get('page', 1))
        size = int(kwargs.get('size', 10))

        filter_list = []
        # 过滤为空的条件
        if num:
            filter_list.append(cls.num == num)

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
    def dle_bbs(cls, **kwargs):
        try:
            num = kwargs.get('num')

            s = session.query(BBsModel).filter(BBsModel.num == num).delete()
            if s == 0:
                print("数据库表中无此id的记录")
                return{'code': RET.DBERR, 'message': '数据库异常，更新失败'}
            else:
                session.commit()

        except Exception as e:
            session.rollback()
            print("数据库表中无此id的记录")
            return {'code': RET.DBERR, 'message': '数据库异常，更新失败', 'error': str(e)}

        return {'code': RET.OK, 'message': 'OK'}

    @classmethod
    def udd_bbs(cls,  **kwargs):
        try:
            num = kwargs.get('num')
            info = kwargs.get('info')

            user_info = session.query(BBsModel).filter(BBsModel.num == num).first()

            if info == 0:
                if user_info.state == 'Done':
                    user_info.state = 'Undo'
                else:
                    user_info.state = 'Done'
            else:
                user_info.content = info

            session.commit()

        except Exception as e:
            session.rollback()
            print("数据库表中无此id的记录")
            return {'code': RET.DBERR, 'message': '数据库异常，更新失败', 'error': str(e)}

        return {'code': RET.OK, 'message': 'OK'}