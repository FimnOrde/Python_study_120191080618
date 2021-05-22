#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class_infomodel.py
# author:74049
# datetime:2021/5/22 21:36
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from sqlalchemy import BigInteger, Column, DateTime, String, and_, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StudentGroup(Base):
    __tablename__ = 'class_info'

    num = Column(Integer, primary_key=True)
    clas = Column(String(20), info='学生班级')
