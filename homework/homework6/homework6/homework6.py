#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework6.py
# author:74049
# datetime:2021/4/17 17:38
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
info_lis = []
class Student(object):
    stuclass = ''
    stuid = ''
    name = ''
    score = 0
    def __init__(self, stuclass, stuid, name, score):
        self.stuclass = stuclass
        self.stuid = stuid
        self.name = name
        self.score = score

class info(object):
    lis = []
    object = []
    def __init__(self):
        self.object = info_lis

    def add_info(self, student):
        self.lis.append(student.stuclass)
        self.lis.append(student.stuid)
        self.lis.append(student.name)
        self.lis.append(student.score)
        self.object.append(self.lis)
        self.lis = []
        with open("D:\\PythonTest\\Test\\homework6\\homework6\\info.txt", 'w', encoding='utf-8')as file:
            string = ""
            for i in info_lis:
                for j in i:
                    string = string + str(j) +" "
                string = string + "\n"
                file.write(string)
                string = ""


    def ser_info(self, stuid):
        for i in info_lis:
            if stuid in i:
                print("此学生信息:")
                info = ""
                for j in i:
                    info = info + str(j) + " "
                return info, i
            else:
                continue
        else:
            lis = ["没有此学生成绩信息"]
            return lis

    def upd_info(self, stuid):
        stu = self.ser_info(stuid)
        if stu[0] != "没有此学生成绩信息":
            print(stu[0])
            inf = input("输入修改后的信息(用空格隔开):").split(" ")
            for i in range(4):
                stu[1][i] = inf[i]

            with open("D:\\PythonTest\\Test\\homework6\\homework6\\info.txt", 'w', encoding='utf-8')as file:
                string = ""
                for i in info_lis:
                    for j in i:
                        string = string + str(j) + " "
                    string = string + "\n"
                    file.write(string)
                    string = ""
            return "修改成功"
        else:
            return "没有此学生成绩信息"

    def del_info(self, stuid):
        stu = self.ser_info(stuid)
        if stu[0] != "没有此学生成绩信息":
            print(stu[0])
            info_lis.remove(stu[1])
            with open("D:\\PythonTest\\Test\\homework6\\homework6\\info.txt", 'w', encoding='utf-8')as file:
                string = ""
                for i in info_lis:
                    for j in i:
                        string = string + str(j) + " "
                    string = string + "\n"
                    file.write(string)
                    string = ""
            return "删除成功"
        else:
            return "没有此学生成绩信息"

info = info()

student1 = Student("2班", "0201", "TOM", 85)
student2 = Student("2班", "0202", "BOB", 95)
student3 = Student("2班", "0203", "JESS", 81)
student4 = Student("2班", "0204", "HORY", 76)
student5 = Student("3班", "0301", "WUU", 93)

info.add_info(student1)
info.add_info(student2)
info.add_info(student3)
info.add_info(student4)
info.add_info(student5)

print(info.ser_info("023")[0])

print(info.upd_info("0202"))

print(info.del_info("0203"))

