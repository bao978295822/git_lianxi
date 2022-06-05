#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/22 17:27
# @Author : bao
# @Site : 
# @File : liebiao.py
# @Software: PyCharm
'''
练习列表的相关操作

'''
# list1 = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
# list2 = [(1, 2, 3), (4, 5, 6)]
# list3=[{1,2,3},{4,7,8}]
# print(type(list1))
# print(type(list2))
# print(type(list3))
import copy

'''
列表推导式
'''
# for i in range(10):
#     if i%2==0:
#         print(i)

# print([i ** 2 for i in range(10) if i % 2 == 0])


# list1 = [1, 2, 3, 4, 54, 5]
# print(type(list1))
# print(len(list1))

# print(list1)

# for i in range(1,10,1):
#     print(i)

# for j in range(1, 10, 3):  # 最后的3是步长，两个数的插值
#     print(j)
#
# for k in range(10):  # 起始位置从0开始
#     print(k)

# list2 = [1, 2, 3,{"a": "b", "c": "d"}]
# print(type(list2))
# print(len(list2))
# print(id(list2))
# print(id(list2[0]))
# print(id(list2[1]))
# print(id(list2[2]))
# print(id(list2[3]))
# list2 = [1, 2, 3,{"a": "b", "c": "d"}]
# list3 = [1, 2, 3,{"a": "b", "c": "d"}]
# # list3=list2.copy()
# # print(list3)
# print(id(list2))
# print(id(list3))
# print(id(list2[0]))
# print(id(list3[0]))
# print(id(1))


# list4=copy.deepcopy(list3)
# print(list4)
# print(id(list4))
# print(id(list3))
# print(id(list4[0]))
# print(id(list3[0]))

'''
列表的查找
'''
# index 根据元素返回下标位置

list4 = [1, 2, 3, 3, 3, 3]
print(list4.index(1))
print(list4.count(34))

if 1 in list4:
    print("1在列表中")
if 11 not in list4:
    print("11不在列表中")

'''
列表，让用户输入数据
判断，如果在，则返回在；不在则返回不在
'''
# name_list=["ceshi","babao","jiawei"]
# name=input("请输入您的名字：")
# if name in name_list:
#     print(f"您输入的名字是{name},存在列表中")
# if name not in name_list:
#     print(f"您输入的名字是{name}，没有存在列表中")

name_list2 = ["ceshi", "babao", "jiawei"]
name_list2.append("xiangqian")
print(name_list2)

