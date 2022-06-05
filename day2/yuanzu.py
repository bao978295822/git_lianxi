#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/21 14:11
# @Author : bao
# @Site : 
# @File : yuanzu.py
# @Software: PyCharm
tup1=(1,2,3,4,5,3,3)
print(type(tup1))
# tup1[0]=2
# print(tup1)
#返回数据所在得下标
print(tup1.index(3))

#计算某个数据个数
print(tup1.count(3))

#计算长度
print(len(tup1))

tup1=(1,2,3,4,5,3,3,[1,2,3])
tup1[7][0]=99
print(tup1)