#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/14 16:55
# @Author : bao
# @Site : 
# @File : tiaojian.py
# @Software: PyCharm
# age=int(input("请输入你的年龄："))
# if age>=18:
#     print(f"你的年龄是{age}岁,可以上网嗨皮")
# else:
#     print(f"你的年龄是{age}岁,回家写作业吧")
# print("回家")

# 根据年龄来判断是否工作
# age = int(input("请输入你的年龄："))
# if 0 <= age < 18:
#     print("童工")
# elif 18 <= age <= 60:
#     print("搬砖")
# elif age > 60:
#     print("可以养老")
# else:
#     print("输入数据非法")


#公交车坐车场景  if嵌套
cash=int(input("座位数："))
if cash>0:
    print("有座")
    seat=int(input("卡余额为："))
    if seat>0:
        print("坐着去")
    else:
        print("站着去")
else:
    print("走着去")