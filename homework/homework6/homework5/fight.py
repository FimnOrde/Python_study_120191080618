#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:fight.py
# author:74049
# datetime:2021/4/17 16:45
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import Dog
import People
import random

dog1 = Dog.Dog()
dog2 = Dog.Dog()
dog3 = Dog.Dog()
people1 = People.People()
people2 = People.People()

list_dog = [dog1, dog2, dog3]
list_people = [people1, people2]

lis = [list_dog, list_people]


while len(list_dog) != 0:
    if len(list_people) != 0:
        dog_num = random.randint(0, len(list_dog)-1)
        people_num = random.randint(0, len(list_people)-1)

        list_dog[dog_num].attack(list_people[people_num])
        print(f'狗{dog_num}攻击人{people_num}')
        print(f'狗{dog_num}生命值{list_dog[dog_num].health_value},人{people_num}生命值{list_people[people_num].health_value}')
        if list_people[people_num].health_value <= 0:
            print(f'人{people_num}死亡,退出游戏')
            list_people.remove(list_people[people_num])
            continue

        list_people[people_num].attack(list_dog[dog_num])
        print(f'人{people_num}攻击狗{dog_num}')
        print(f'人{people_num}生命值{list_people[people_num].health_value},狗{dog_num}生命值{list_dog[dog_num].health_value}')
        if list_dog[dog_num].health_value <= 0:
            print(f'狗{dog_num}死亡,退出游戏')
            list_dog.remove(list_dog[dog_num])
            continue
    else:
        break
