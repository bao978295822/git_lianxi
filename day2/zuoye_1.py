#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/23 21:42
# @Author : bao
# @Site : 
# @File : zuoye_1.py
# @Software: PyCharm
''''
1.需求：有三个办公室，8位老师，8位老师随机分配到3个办公室
第一间的老师是b
'''
import random

teacher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
room1 = [[], [], []]  # room1[room][i]
# 获取8位老师
for i in teacher:
    room = random.randint(0, 2)
    room1[room].append(i)
# print(room1)
m=0
print("第1题")
for j in room1:
    # print(j)

    print(f"第{m+1}个教室,有老师{len(j)}人")
    m+=1
    for k in j:
        print(k,end='\t')
    print("")
    # j=0
    # print(f"第{j+1}个教室")
    # j+=1
    # for name in k:
    #     print(name,end="\t")

#
# for j in room1:
#     # for k in range(3):
#     #     print(f"第{k+1}个教室，里面有{j}这几位老师")
#     #     break
#     # k=0
#     # while k<3:
#     #     print(f"第{k+1}个教室，里面有{j}这几位老师")
#     #     k+=1
#     #     break
#     print(j)