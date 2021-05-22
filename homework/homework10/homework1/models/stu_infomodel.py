#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:stu_infomodel.py
# author:74049
# datetime:2021/5/22 21:37
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from sqlalchemy import BigInteger, Column, DateTime, String, and_, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentGroup(Base):
    __tablename__ = 'stu_info'

    num = Column(Integer, primary_key=True)
    name = Column(String(20), info='学生姓名')
    age = Column(Integer, info='学生年龄')
    gender = Column(String(50), info='学生性别')
    isdeleted = Column(Integer, info='信息是否删除')