#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/18 22:06
# @Author : bao
# @Site : 
# @File : for1.py
# @Software: PyCharm

'''

for循环
i是变量,有几个字符串就循环即便
a1是list列表
'''

# a1=["a","b","c","d"]
# for i in a1:
#     print(i)

'''
练习break
continue
'''
# i=1
# while i<=5:
#     if i==4:
#         print("吃饱了，不吃了")
#         break
#     print(f"吃的是第{i}个苹果")
#     i+=1
#
# i=1
# while i<=5:
#     if i==4:
#         print(f"吃的第{i}个苹果有虫子，不吃这个了")
#         i += 1
#         continue
#
#     print(f"吃的是第{i}个苹果")
#     i+=1


list=["a","b"]
tupple=("aa","bb")
set={"aa","bb"}
dict={"aa":"1"}

# print(type(list))
# print(type(tupple))
# print(type(set))
# print(type(dict))
# set.update("100")
set.update(100)
print(set)