#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/21 16:13
# @Author : bao
# @Site : 
# @File : gonggong.py
# @Software: PyCharm

# a=[1,3,5,6,33,2,4]

# print(max(a))
# print(min(a))

# for i in range(10):
#     print(i,end ="\t")
#
# for i in range(3,9,2):
#     print(i)
# list1=range(20)
# list1=list(list1)
# print(list1)
#
# for i in a:
#     print(i)

list2=['a','b','c','c']
# for i in enumerate(list2):
#     print(i)

for m,n in enumerate(list2,start=10):
    print(m,n)

list3=[10,10,40,30]
print(list3)
list3=set(list3)
print(list3)