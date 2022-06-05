#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/26 20:05
# @Author : bao
# @Site : 
# @File : list1.py
# @Software: PyCharm
'''
加法的函数
'''
# def sum1(i, j):
#     return i + j
#
#
# i = int(input("请您输入i值："))
# j = int(input("请您输入j值："))
# sum2 = sum1(i, j)
# print(f"你输入的两个数的和为{sum2}")


list1 = ["ceshi", "bao", "weijia", "dupeng", "bao", "bao"]
print(list1.index("bao", 0, 2))
print(list1.count("bao"))
print(len(list1))

print("weijia" in list1)

print("bao2" in list1)

# print("bao2" not in list1)  # 不在列表种，返回bool值
# print("bao" not in list1)
# name = input("请您输入你要查找的名字：")
# if name in list1:
#     print(f"你输入的名字是{name}，存在系统中")
# else:
#     print(f"你输入的名字是{name},不存在系统中")

'''
追加数据
'''
list2 = ["ceshi", "bao", "weijia", "dupeng", "bao", "bao"]
list3=["ceshi", "ceshi22", "xiangqian"]
list2.append(list3)
print(list2)
print(list2[6][1])

#extend
list2.extend("ceshi")
print(list2)

list4=[i for i in list2]
print(list4)