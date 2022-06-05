#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/30 21:58
# @Author : bao
# @Site : 
# @File : zuoye3.py
# @Software: PyCharm
'''
1.使用列表推导式生成能被5整除的数（100以内）

'''


def hanshu():
    list1 = [i for i in range(1, 101) if i % 5 == 0]
    return list1


liebiao = hanshu()
print(f"第一题：100以内能被5整除的数有：{liebiao}")
'''
2.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
'''
name=["tom","ceshi","xiaoming","ceshi22"]
age=[20,19,27,18]
set1={}
for i in range(len(name)):
    set1[name[i]]=age[i]
print(set1)


