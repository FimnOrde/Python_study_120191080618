#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:class21_exercise1.py
# author:74049
# datetime:2021/5/14 19:22
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import MySQLdb
import time
from multiprocessing import Pool

db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='2349@zzh',
    db='mysqldriver_test',
)

search_sql = "SELECT * FROM temp_icp_for_website_spider"
insert_sql = "INSERT INTO mysqlclient VALUES  (%s,%s,%s,%s,%s)"


def search():
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        # 执行sql查询语句
        cursor.execute(search_sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        results = [result[0:5] for result in results]
    except Exception as e:
        print(e)
        return None
    finally:
        cursor.close()
    return results[:10000]


def insert(info):
    cursor = db.cursor()
    try:
        cursor.execute(insert_sql, info)
        db.commit()
    except:
        db.rollback()


if __name__ == '__main__':
    infos = search()
    po = Pool(6)
    start_time = time.time()
    for info in infos:
        po.apply_async(insert, (info,))
    po.close()
    po.join()
    end_time = time.time()
    print("共100000条数据，用时：", end_time - start_time)

# 共100000条数据，用时： 49.747719526290894