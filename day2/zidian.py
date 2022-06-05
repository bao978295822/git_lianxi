#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/21 14:28
# @Author : bao
# @Site : 
# @File : zidian.py
# @Software: PyCharm
# dict1={"name":"tom","age":18}
# print(dict1["name"])
#
# #增加
# dict1["name"]="ceshi"
# print(dict1)
# dict1["country"]="美国"
# print(dict1)
#
# #删除
# # del dict1
# # print(dict1)
# del dict1["name"]
# print(dict1)
#
# dict1.clear()
# print(dict1)

# dict1={"name":"tom","age":18}
#
# #查找
# print(dict1["name"])
# # print(dict1["names"])
#
# #使用get查找
# print(dict1.get("name","没有这个人"))

dict1={"name":"tom","age":18,"genter":"meiguo"}
print(dict1.keys())
key_list=list(dict1.keys())
print(key_list)
print(dict1.values())
print(dict1.items())

# for i in dict1.keys():
#     print(f"键是：{i}")
# for j in dict1.values():
#     print(f"值是：{j}")
for m in dict1.items():
    print(m)
for m1,n1 in dict1.items():
    print(f"键是{m1}，值是{n1}")