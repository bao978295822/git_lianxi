#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/21 20:35
# @Author : bao
# @Site : 
# @File : zuoye2.py
# @Software: PyCharm
''''
1.需求：有三个办公室，8位老师，8位老师随机分配到3个办公室
'''
import random

teacher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
room1 = [[], [], []]  # room1[room][i]
# 获取8位老师
for i in teacher:
    room = random.randint(0, 2)
    room1[room].append(i)
# print(room1)
m = 0
print("第1题")
for j in room1:
    # print(j)

    print(f"第{m + 1}个教室,有老师{len(j)}人")
    m += 1
    for k in j:
        print(k, end='\t')
    print("")

'''
2、求100以内能被3整除的数，并将作为列表输出
首先遍历1-100
if判断
能被3整除，插入到100中
'''
new_list2 = []
for i in range(1, 101):
    # print(i)
    if i % 3 == 0:
        new_list2.append(i)
print(f"第2题：{new_list2}")

'''
3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表  #不允许用强制类型转化
运用if判断，这个元素是否存在当前列表中
如果存在不执行
不存在，往表里插入
'''
list1 = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7]
new_list = []
for i in list1:
    # print(i,end="\t")
    if i not in new_list:
        new_list.append(i)
    # else:
    #     # print("不插入数据")
    #     continue
print(f"第3题：去重后新的列表是 {new_list}")

'''
4、求斐波那契数列 1 1 2 3 5 8 13 ……
定义两个变量？

'''
# list2=[1,1,2,3,5,8,13]   #不需要list2
i = 1
j = 1
new_list3 = [1, 1]

for i in new_list3:
    if j < 100:
        # print(i)
        j += i
        new_list3.append(j)
print(f"第4题：{new_list3}")

'''
5、求100以内的质数（只能被1和它本身整除）
遍历1-100
然后定义变量赋值
'''
new_list4 = []
for i4 in range(5, 100):
    # print(i4)
    # if i4 % 1 == 0 and i4 % i4 == 0:
    #     print(i4)
    if i4 == 2:
        new_list4.append(2)
    for j in range(2, i4):
        # print(j,end="\t")
        # break
        if i4 % j == 0:
            break
        else:
            if (j == i4 - 1):
                new_list4.append(i4)
        # new_list4.append(i4)
        # break
    # continue    #这是debug调出来的
    # print("")
print(f"第5题{new_list4}")

'''
6、有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef #不允许用类型转化
'''
str1 = "aabbbcddef"
str2 = ""
# str1.count(i)
for i in str1:
    # print(i)
    if str1.count(i) > 1:
        continue
    else:
        str2 += i
print(f"第6题：{str2}")

'''
7、有一堆字符串，“welocme to super&Test”，打印出superTest，#不能查字符的索引
首先用空格进行分割，得到三个单词
'''
str7 = "welocme to super&Test"
str_xin7 = str7.split(" ")
for i in str_xin7:
    if "&" in i:
        # print(i)
        i1 = i.split("&")
        # print(i1)
        xin = "".join(i1)
print(f"第7题：{xin}")

'''
8、有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot  #不允许用reverse,和reversed
'''
str8 = "welocme to super&Test"
str_8 = str8.split("welocme")
# print(str_8)
str_9 = " ".join(str_8)
# print(str_9)
str9_xin = str_9[::-1]
print(f"第8题：{str9_xin}")
# for i in str8:
#     print(i)

'''
9、有一堆字符串，“abcdef”，将首尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现,不允许用步长
'''
str1 = "abcdef"
list1 = list(str1)
list2 = []
# print(list1)
for i in range(6):
    list2.append(list1[len(list1) - i - 1])
xin = "".join(list2)
print(f"第9题：{xin}")

'''
10、有一堆字符串，“aabbbcddef”，输出abcdef # 不允许用set
'''
str5 = "aabbbcddef"
str6 = ""
for i in str5:
    if i in str6:
        continue
    else:
        str6 += i
print(f"第10题：输出的字符串{str6}")
