#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class21_exercise4.py
# author:74049
# datetime:2021/5/15 11:22
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

import sqlalchemy

'''
   探究SQLAchemy查询返回的数据类型以及输出问题
'''
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

class Website(Base):
    __tablename__ = 'website'

    id=sqlalchemy.Column(sqlalchemy.INTEGER,primary_key=True)
    name=sqlalchemy.Column(sqlalchemy.String(50))

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user_info'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:648175@localhost:3306/user')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建Session:
session = DBSession()

# 创建Query查询，filter是where条件，最后调用first()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='03').first()

# 查看返回的数据类型
print('type:', type(user))    # 返回的是一个User对象


print(user.id,user.name)
#

def main():
    # 初始化数据库连接:
    engine = create_engine('mysql+pymysql://root:648175@localhost:3306/user')

    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    session=DBSession()
    new_site = Website(id=2, name="www.163.com")
    session.add(new_site) # 添加到session
    session.commit()  # 提交即保存到数据库
    session.close()  # 关闭session
    print('插入数据成功！')

users=session.query(User).all()
print('type:', type(users))

for user in users:
    print(user.id,user.name)

if __name__ == '__main__':
    main()