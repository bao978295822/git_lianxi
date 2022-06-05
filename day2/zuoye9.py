#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/23 20:36
# @Author : bao
# @Site : 
# @File : zuoye9.py
# @Software: PyCharm
'''
9、有一堆字符串，“abcdef”，将首尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现,不允许用步长
'''
# str1="abcdef"
# list1=list(str1)
# list2=[]
# # print(list1)
# for i in range(6):
#     list2.append(list1[len(list1)-i-1])
# # print(list2)
# # str_xin2=[]
# # print(str_xin)
# # for i in list2:
# #     str_xin2.append(i)
# #     # str_xin2+=i
# # print(str_xin2)
# xin="".join(list2)
# print(xin)


'''
9、有一堆字符串，“abcdef”，将首尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现,不允许用步长
'''
# str1="abcdef"
# list1=list(str1)
# list2=[]
# # print(list1)
# for i in range(6):
#     list2.append(list1[len(list1)-i-1])
# xin="".join(list2)
# print(xin)


'''
9、有一堆字符串，“abcdef”，将首尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现,不允许用步长
下面是废弃的代码
'''
# str_jiu = "abcdef"
# list_jiu = list(str_jiu)
# list_xin = []
# str_fanzhuan = ""
# for i in list_jiu:
#     # 得到了每个元素
#     # print(i)
#     # list_jiu.append(len(str_jiu)-1) == i
#     for j in range(5):
#         list_jiu[len(str_jiu) - j] == i
#     # list_jiu[len(str_jiu) - i] == i
#     print(len(str_jiu) - 1)
# str_jiu[len(str_jiu)-1]=i
# print(len(str_jiu))
# print(str_fanzhuan)
# print(str_jiu(len(str_jiu)))
# str_jiu[0] = "c"
# # print(str_jiu)
# print(list_jiu)


'''
9、有一堆字符串，“abcdef”，将首尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现,不允许用步长
下面是废弃的代码
'''
str1 = "abcdef"
# for k in str1:
#     print(k,end="")
print(list(str1))
# list1=list[str1]
# print(list1)
# print(type(list1))
# str2 = []
# for i in range(5):
#     # print(i)
#     str1[5 - i] = str1[i]
#     str2.append(5 - i)
