#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/20 22:27
# @Author : bao
# @Site : 
# @File : hanshu3.py
# @Software: PyCharm

def jieshou(i, j):
    return i * j, i + j


a ,b=jieshou(2,3)
# a = jieshou(3, 4)  # 打印的是元组类型的数据
print(a,b)

def bijiao(a,b):
    v=a if a>b else b
    return v
i=bijiao(10,5)
print(i)
max()