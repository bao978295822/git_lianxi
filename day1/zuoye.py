#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/15 17:38
# @Author : bao
# @Site : 
# @File : zuoye2.py
# @Software: PyCharm

'''
1.重新操作课程中学习的所有代码
2.完成教程中未实现的作业:石头剪刀布
3.正方形,三角形,九九乘法表
4.三角形的不同样子（右对齐，等腰三角形）
'''

# # 2石头剪刀布的游戏
import random


# 石头0  剪刀1   布2
wanjia = int(input("玩家请输入石头剪刀布："))  # 需转int,不转有bug
computer = random.randint(0, 2)
# computer=input("请输入石头剪刀布：")
print(f"电脑是{computer}")

if wanjia == 0 and computer == 1:
    print("玩家胜利了，电脑输了")
elif wanjia == 1 and computer == 2:
    print("玩家胜利了，电脑输了")
elif wanjia == 2 and computer == 0:
    print("玩家胜利了，电脑输了")
elif wanjia == computer:
    print("玩家和电脑打成了平局")
else:
    print("电脑赢了，玩家输了")

# 3 打印九九乘法表
ii = 1  # i代表行数吧
while ii <= 9:
    ji = 1
    while ii>=ji:
        print(f"{ji}*{ii}={ii*ji}",end='    ')
        ji+=1
    ii+=1
    print(end='\n')

# 3 打印正方形
i1=1    #行数
while i1<=5:
    j1=1
    while j1<=5:
        print("*",end="")
        j1+=1
    i1+=1
    print("")
#
# # 3 打印三角形
i2=1    #行数
while i2<=5:
    j2=1
    while i2>=j2:
        print("*",end="")
        j2+=1
    i2+=1
    print("")


# # 4.打印右对齐的正三角形
line = 5    #行数
i = 1
while i <= line:
    j = 1   #空格数

    while j < 6 - i:  #
        print(" ", end="")
        j += 1
    k = 1   #星星数
    while k < i + 1:  #右对齐的三角形
    # while k < 2*i - 1:  #等腰
        print("*", end="")
        k += 1
    print("")
    i += 1


# #4.打印等腰三角形
line = 5    #行数
i = 1
while i <= line:
    j = 1   #空格数

    while j < line - i:  #
        print(" ", end="")
        j += 1
    k = 1   #星星数
    # while k < i + 1:  #右对齐的三角形
    while k <= 2*i - 1:
        print("*", end="")
        k += 1
    print("")
    i += 1