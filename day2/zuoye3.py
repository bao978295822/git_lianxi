#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/23 8:49
# @Author : bao
# @Site : 
# @File : zuoye3.py
# @Software: PyCharm

'''
3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表  #不允许用强制类型转化
count  这种方式不行

'''
# list1 = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7]
# new_list = []
# for i in list1:
#     # print(new_list.count(i))
#     # print(list1.count(i))
#     if  list1.count(i)>1:
#         continue
#     else:
#         new_list.append(i)
# print(new_list)

# print(list1[0])
# print(list1[1])

'''
需求：有三个办公室，8位⽼师，8位⽼师随机分配到3个办公
教师使用随机数0-2
遍历8位老师
'''
# import random
# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# room=[[],[],[]]
# for i in list1:
#     # print(i)
#     suiji=random.randint(0,2)
#     # print(suiji)
#     room[suiji].append(i)
# print(room)

# list2=[1,1,2,3,5,8,13]
# i=1
# j=1
# new_list3=[1,1]
#
# for i in new_list3:
#     # print(i)
#     j += i
#     new_list3.append(j)
# print(new_list3)

