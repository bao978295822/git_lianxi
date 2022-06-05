#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/14 18:07
# @Author : bao
# @Site : 
# @File : xunhuan.py
# @Software: PyCharm

# 道歉5次
# i=0
# while i<5:
#     print("我错了")
#     i+=1


# 实现1-100相加
# i=0
# sum = 0
# while i<=3:
#     sum+=i
#     i+=1
# print(sum)

# 实现1-100偶数相加
# i=0
# sum = 0
# while i<=3:
#     sum+=i
#     i+=1
# print(sum)

# i=1
# sum=0
# while i<=5:
#     print(f"吃的第{i}个苹果")
#     i+=1

# break
# i=1
# sum=0
# while i<=5:
#     if i==3:
#         print("不吃了")
#         break
#     print(f"吃的第{i}个苹果")
#     i+=1

# continue
# i=1
# sum=0
# while i<=5:
#     if i==3 or i==4:
#         print(f"第{i}个苹果有虫子，不吃了")
#         i+=1
#         continue
#     print(f"吃的第{i}个苹果")
#     i+=1

# i=0
# while i<3:
#     print("我错了")
#     i+=1
# print("刷了今天的碗")

# #打印的正方形
# i=0
# while i<5:
#     j=0
#     while j<5:
#         print("*", end='')
#         j+=1
#     print("")
#     i+=1

# 打印的正三角形
# i = 1  # 行数
# while i < 5:
#     j = 0
#     while j < i:
#         print("*", end='')
#         j += 1
#     print("")
#     i += 1

# str="hello"
# for i in str:
#     if i=="l":
#         print("不打印")
#         break
#         # continue
#     print(i)

# n=1
# while n<=5:
#     if n==3:
#         print("道歉不真诚")
#         n += 1
#         # break
#         continue
#     print("我错了")
#     n+=1
# else:
#     print("原谅我了")
#     n+=1

str="hello"
for i in str:
    if i=="l":
        print("这次不打印")
        break
        # continue
    print(i)
else:
    print("执行完毕")