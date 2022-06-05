#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/19 19:49
# @Author : bao
# @Site : 
# @File : jihe.py
# @Software: PyCharm

# set={"aa","bb"}
# # set.update(100)
# set.update("12")
# print(set)
#
#
# '''
# 三目运算符
# '''
# a=10
# b=4
# c=a if a>b else b
# print(c)


name = "abcdefg"
print(id(name))
a = name
print(id(a))

# 输出我的名字是宝，我的年龄22岁了
name = "宝"
age = 22
print("我的名字是%s,我的年龄%d岁" % (name, age))

str1 = '11'
tupple = '("aa","bb")'
list = '[1,2,3]'
print(type(eval(str1)))
print(type(eval(tupple)))
print(type(eval(list)))

print(1 * 4)
print(2 ** 3)

a = 12
b = 13
c = 20
print(a == b)
print(a != b)

print((a > b) and (b< c))
print((a > b) or (b< c))





