#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/18 21:33
# @Author : bao
# @Site : 
# @File : caiquan.py
# @Software: PyCharm

'''
写一个玩家和电脑猜拳的游戏
石头 0
剪刀  1
布   2
'''

import random
wanjia=int(input("玩家请输入石头剪刀布:"))
computer=random.randint(0,2)
print(f"电脑出的是{computer}")
if wanjia==0 and computer==1:
    print("玩家胜利")
elif wanjia==1 and computer==2:
    print("玩家胜利")
elif wanjia==2 and computer==0:
    print("玩家胜利")
elif wanjia==computer:
    print("玩家和电脑打成了平局")
else:
    print("电脑胜利了,玩家输了")