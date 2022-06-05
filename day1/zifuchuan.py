#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/14 15:17
# @Author : bao
# @Site : 
# @File : zifuchuan.py
# @Software: PyCharm
# a='fafd'
# tupple="iiii"
# print(type(a))
# print(type(tupple))

#下标
# name='abcdefg'
# # print(name[0])
# # print(name[1])
# print(name[2:5:1])
# print(name[2:5])
# print(name[:5])
# print(name[1:])
# print(name[:])
# print(name[::2])
# print(name[:-1])
# print(name[-4:-1])
# print(name[::-1])


# mystr = "hello world and superctest and chaoge and Python"

# print(mystr.find("and"))
# print(mystr[12])
# print(mystr[20])
# print(mystr.find("and",13,20))
# print(mystr.find("ands"))
#
# print(mystr.index("and"))
# # print(mystr.index("ands"))
#
# print(mystr.count("and"))
# print(mystr.count("and",15,40))
# print(mystr.count("ands"))

# print(mystr.rfind("n"))

# mystr = "hello world and superctest and chaoge and Python"
# print(mystr.split("and"))
# print(mystr)

# #替换
# print(mystr.replace("and","AND"))
# print(mystr.replace("and","AND",2))
# print(mystr)
#
# #分割
# print(mystr.split("and"))
# print(mystr.split("and",2))
# print(mystr.split(" "))
#
# #拼接
# print(mystr.join("-"))



# mystr = "             hello world and superctest and chaoge and Python            "
# print(mystr.strip())
# print(mystr.lstrip())
# print(mystr.rstrip())
#
# #补充字符
# str1="hello"
# print(str1.ljust(20,"-"))
# print(str1.rjust(20,"*"))
# print(str1.center(20,"*"))

#判断是否以字符串开头
# mystr = "hello world and superctest and chaoge and Python"
# print(mystr.startswith("hello"))
# print(mystr.startswith("hello",4,20))


mystr = "hello world and superctest And chaoge and Python"
# print(mystr.find("super"))  #17
# print(mystr[0])
# print(mystr.find('and',12,20))
# print(mystr.find("ands"))   #子串不存在，返回-1
#
# #index的用法
# print(mystr.index("ands"))
# print(mystr.index("hello",0,5))

# #count 计算字串数量的方法
# print(mystr.count("and"))
# print(mystr.count("ands"))
# print(mystr.count("and",0,15))

# #replace 替换
# print(mystr.replace("and","AND",4))
# print(mystr)    #不改变原字符串
#
# print(mystr.split("e")) #通过为e来分割字符串
# print(mystr)
#
# print(mystr.split(" "))
#
#
# print(mystr.join("aa"))
#
# list1=["aa","bb","cc","dd"]
# print("__".join(list1))
# print("-".join(list1))
#
# print(mystr.capitalize())   #把字符串的首个字母转换成大写
# print(mystr.title())
# print(mystr.lower())
# print(mystr.upper())
#
# print(mystr.startswith("hello"))
# print(mystr.startswith("hello1"))
#
# print(mystr.endswith("python"))
# print(mystr.endswith("Python"))
''''
List列表的练习
'''
# name_list=['tom','jetrry','bao']
# name=input("请输入你的名字：")
# if name in name_list:
#     print(f"你的名字在列表中,你输入的名字是{name}")
# else:
#     print(f"你的名字不在列表中，你输入的名字是{name}")
# name1="lisi"
# name_list.append(name1)
# print(name_list)


'''
判断是否能上公交车
是否有钱
是否有座
'''
money=int(input("公交卡的余额为："))
if money>0:
    print(f"公交卡的余额为{money}元")
    seat = int(input("剩余的座位数："))
    if seat>0:
        print(f"公交车上剩余的座位为{seat}")
    else:
        print("公交车没有座位了")
else:
    print("你的公交卡没有余额了，不能上车")





