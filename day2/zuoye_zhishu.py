#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/22 23:00
# @Author : bao
# @Site : 
# @File : zuoye_zhishu.py
# @Software: PyCharm
'''
5、求100以内的质数（只能被1和它本身整除）
遍历1-100
然后定义变量赋值
'''
new_list4 = []
for i4 in range(5, 100):
    if i4 == 2:
        new_list4.append(2)
    for j in range(2, i4):
        if i4 % j == 0:
            break
        else:
            if (j == i4 - 1):
                new_list4.append(i4)
print(new_list4)