#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/21 15:01
# @Author : bao
# @Site : 
# @File : jihe.py
# @Software: PyCharm

s1 = {1, 2, 3, 4, "a", "b", 5, 6, 7}
s2 = {1, 2, 3, 4, "a", "b", 5, 6, 7, 7, 7, 7, 7, 8}
# print(s1)
# print(s2)
#
# set1 = set()
# print(type(set1))
# s1.add(20)
# print(s1)
# s1.add(1)
# print(s1)
# s3=(99,88)
# s1.update(s3)
# print(s1)



#删除
s3={"bbb", "a", "b", 6, 7}
# s3.remove("a")
# print(s3)
# # s3.remove("fsadj")
# # print(s3)\
#
# #删除
s3={"bbb", "a", "b", 6, 7}
# s3.discard(6)
# print(s3)
# s3.discard(999)
# print(s3)

#随机删除

print(s3.pop())
print(s3)

