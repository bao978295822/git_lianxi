#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/14 10:54
# @Author : bao
# @Site : 
# @File : t1.py
# @Software: PyCharm
'''
1、练习输出
2、注释
'''

# 输出hello world
# 第一行代码

'''
测试多行注释

测试测试11111
测试内容
'''
# print("hello world!")
# print('hello world!')
# # print(hello world!)
#
#
#
# #0517日练习：f表达式
# #我的名字是宝， 明年的年龄是20岁
# name='宝'
# age=19
# print(f"我的名字是{name}，明年的年龄是{age+1}岁")
#
# a="I'm Tom "
# print(a)
# list1=[1,2,3]
# print(type(list1))

'''
转换成浮点型
转换成字符串
将一个list转换成元组
把tupple转换成列表

'''
# a1 = 1
# print(type(float(a1)))  # 转换成浮点型
# print(float(a1))
#
# str1=11
# print(type(str(str1)))  #转换成字符串
#
# tup=[1,2,3,4]
# print(type(tuple(tup))) #将一个list转换成元组
# print(tuple(tup))   #打印tupple
#
# l1=(1,2,3,3,3,3)
# print(type(list(l1)))   #把tupple转换成列表
# print(list(l1))     #打印转换的列表

# name="abcdefg"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])


# 需求 cde
# cde
# abcde
# bcdefg
# abcdefg
# aceg
# abcdef, 负1表示倒数第⼀个数据
# def
# gfedcba
a = "abcdefg"
print(a[2:5])  # 需求 cde
print(a[0:5:1])  # 需求 cde  加上了步长
print(a[:5])    # abcde 前5个
print(a[1:])   # bcdefg 从下表1开始后面的
print(a[::])    # abcdefg
print(a[::2])   # aceg
print(a[:-1])   # abcdef, 负1表示倒数第⼀个数据
print(a[-4:-1]) # def   容易出错

print(a[::-1])  # gfedcba  数据倒着排

aa="""
测试多行内容显示
1243232
fhsdakfadljf
"""
print(aa)
print(type(aa))



