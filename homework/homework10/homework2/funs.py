#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:funs.py
# author:74049
# datetime:2021/5/22 22:50
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from homework2 import connector
import pymysql


db, cursor = connector.cnc()

def insert(info):
    # SQL 插入语句
    sql = 'INSERT INTO COMMENTBOARD(ID, CONTENT, COMMENTATOR, CTIME, ISDELETED) VALUES ("%s", "%s", "%s", NOW(), 0)' % info
    try:
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("插入成功")
    except:
        print("数据库打开出错")
    db.close()


def delet(id):
    sql = "DELETE FROM COMMENTBOARD WHERE ID = %s" % (id)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
        print("删除成功")
    except:
        print("没有此id的记录")
        # 发生错误时回滚
        db.rollback()
    # 关闭连接
    db.close()

def updt(info, id):
    info.append(id)
    info = tuple(info)
    sql = "UPDATE COMMENTBOARD SET ID = '%s',CONTENT = '%s',COMMENTATOR = '%s',CTIME = NOW(),ISDELETED = %s WHERE ID = '%s'" % info
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print('更新成功')
    except:
        print('没有此id的记录')

    # 关闭数据库连接
    db.close()

def src(id):
    sql = "SELECT * FROM COMMENTBOARD \
           WHERE ID = %s" % id
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print("id=%s,内容=%s,发送者=%s,时间=%s,是否删除=%s" % \
                  (fname, lname, age, sex, income))
    except:
        print("Error: unable to fetch data")

if __name__ == '__main__':
    print('-'*5, '插入一条记录', '-'*5)
    # info = ('03', 'contents', 'BELL')
    # insert(info)

    print('-' * 5, '更新一条记录', '-' * 5)
    # info1 = ['03', 'contt', 'BELL', 0]
    # updt(info1, '03')

    print('-' * 5, '查询一条记录', '-' * 5)
    # src('03')

    print('-' * 5, '删除一条记录', '-' * 5)
    # delet('03')



