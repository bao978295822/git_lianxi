#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/25 21:34
# @Author : bao
# @Site : 
# @File : fenpeijs.py
# @Software: PyCharm
'''

需求：有三个办公室，8位⽼师，8位⽼师随机分配到3个办公室
使用随机函数
最终输出格式
第一个房间：几人
老师有哪几位[,,]
'''
import random

teachers = ["a", "b", "c", "d", "e", "f", "g", "h"]
jiaoshi = [[], [], []]
for teac in teachers:  # 把每一位老师从列表中遍历出来
    # print(teac)
    fangjian = random.randint(0, 2)
    jiaoshi[fangjian].append(teac)
# print(jiaoshi)
# for i in range(1,4):
# print(i)
# print(i)
j = 1
for i in jiaoshi:
    print(f"第{j}个房间，里面有{len(jiaoshi[j - 1])}个教师")
    print(f"房间里的老师是：{i}")
    j += 1