#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/14 13:47
# @Author : bao
# @Site : 
# @File : shuchu.py
# @Software: PyCharm
# name='tom'
# age=18
# weight=75.5
# stu_id=1
# print("我的名字是%s"% name)
# print("我的年龄是%d岁" % age)
# print("我的体重是%.3f公斤" % weight)
# print("我的名字是%s,今年%d岁" % (name,age))
# print("我的名字是%s，我的年龄是%d"% (name,age+1))
# print(f"我的姓名是{name},我的年龄是{age+5}")


# print("123",end='\t')
# print("456",end='--')
#
# print(r"123\n456")


name = '宝'
student_id = 1
weight = 75.5
age = 18

print("我的名字是%s" % name)  # 我的姓名是宝
print(f"我的名字是{name}")  # 我的姓名是宝，另一种写法

print("我的学号是%04d" % student_id)  # 我的学号是0001
print("我的体重是%.2f" % weight)
print(f"我的名字是{name},今年的年龄是{age}岁")  # 我的名字是宝,今年的年龄是18岁
print(f"我的名字是{name},明年的年龄是{age + 1}")  # 我的名字是宝,明年的年龄是19
