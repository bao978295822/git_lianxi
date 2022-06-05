#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/14 14:18
# @Author : bao
# @Site : 
# @File : zhuanhuan.py
# @Software: PyCharm
name = 55
data = "name"
data1 = eval(data)
print(type(data1))

str1 = '10'
str2 = '[1,2,3,34]'
str3 = '(1,2,23,4)'
# print(type(eval(str1)))
# print(type(eval(str2)))
# print(type(eval(str3)))

num = 1
print(float(num))

num2 = 22
print(type(str(num2)))

list1 = [1, 2, 3]
print(type(tuple(list1)))

t1 = (12, 3, 4)
print(type(list(t1)))

#---------------------------下面是练习的代码
a1 = '11'
print(type(eval(a1)))  # int

list1 = '[1,33]'
print(type(list1))  # str1
print(type(eval(list1)))  # list

tupple1 = '(1,2,1,1)'
print(type(eval(tupple1)))  # tupple元组

set='{1,2,3,3,3}'
print(type(eval(set))) #set集合

dict2 = "{'a':'1'}"
print(type(eval(dict2)))  # dict字典
