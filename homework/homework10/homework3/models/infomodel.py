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
    __tablename__ = 'commentboard'

    id = Column(String, primary_key=True)
    content = Column(String(255, 'utf8_general_ci'), info='留言信息')
    commentator = Column(String(255, 'utf8_general_ci'), info='留言者')
    ctime = Column(DateTime, server_default=FetchedValue(),primary_key=True)
    isdeleted = Column(Integer,  info=0)

    @classmethod
    def add_bbs(cls, **kwargs):
        try:
            bbs_model = BBsModel(
                commentator=kwargs.get('commentator'),
                content=kwargs.get('content'),
                ctime=kwargs.get('ctime'),
                isdeleted = kwargs.get('isdeleted'),
                id=kwargs.get('id')
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
        id = kwargs.get('id')
        page = int(kwargs.get('page', 1))
        size = int(kwargs.get('size', 10))

        filter_list = []
        # 过滤为空的条件
        if id:
            filter_list.append(cls.id == id)

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
            id = kwargs.get('id')

            s = session.query(BBsModel).filter(BBsModel.id == id).delete()
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
    def udd_bbs(cls, dic, **kwargs):
        try:
            id = kwargs.get('id')

            user_info = session.query(BBsModel).filter(BBsModel.id == id).first()

            user_info.id = dic['id']
            user_info.commentator = dic['commentator']
            user_info.content = dic['content']
            user_info.isdeleted = dic['isdeleted']
            user_info.ctime = dic['ctime']

            session.commit()

        except Exception as e:
            session.rollback()
            print("数据库表中无此id的记录")
            return {'code': RET.DBERR, 'message': '数据库异常，更新失败', 'error': str(e)}

        return {'code': RET.OK, 'message': 'OK'}