#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/21 16:33
# @Author : bao
# @Site : 
# @File : tuidao.py
# @Software: PyCharm

# 列表推导式
# 创建一个0-10得列表
# list1 = []
# i = 0
# while i <= 10:
#     if i%2==0:
#         list1.append(i)
#     i += 1
# print(list1)
#
# list2 = []
# for i in list1:
#     if i%2==0:
#         list2.append(i)
# print(list2)
#
# # list3 = [i for i in range(11)]
# # print(list3)
#
# #列表推导式，只取0-10得偶数
# list4 = [i for i in range(11) if i % 2 == 0]
# print(list4)

# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)
# list5=[]
# for i in range(1,3):
#     # print(i)
#     for j in range(3):
#         list5.append((i,j))
# print(list5)

# list6=[(m,n) for m in range(1,3) for n in range(3)]
# print(list6)

# dict1 = {k: k ** 2 for k in range(1,4)}
# print(dict1)


#把两个列表快速合并成字典
# list1=['name','age','sex']
# list2=['ceshi',20,'女']
# dict2={}
# for i in range(len(list1)):
#     # list1[i]=list2[i]
#     dict2[list1[i]]=list2[i]
# print(dict2)

# dict3={list1[i]:list2[i] for i in range(len(list1))}
# print(dict3)
#
# counts={'mbp':300,'hp':250,"dell":100,"aaa":400}
# dict1={}
# # for i in range(len(counts)):
# for i in counts:
#     if counts[i]> 270:
#         dict1[i]=counts[i]
# print(dict1)
#
# dcit2={k:v for k,v in counts.items() if v>270}
# print(dcit2)


# list1=[1,1,3,9,3]
# # set1={i ** 2 for i in list1}
# # print(set1)
# print(id(list1))
# print(id(list1[0]))
# print(id(list1[1]))
# print(id(list1[2]))

import copy
list2=[1,2,[66,77]]
list3=copy.deepcopy(list2)
print(list2)
print(list3)
print(id(list2[-1]))
print(id(list3[-1]))

list3=[1,2,[66,77]]
list4=list3.copy()
print(list3)
print(list4)
print(id(list3[-1]))
print(id(list4[-1]))