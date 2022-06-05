#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/20 21:51
# @Author : bao
# @Site : 
# @File : hanshu2.py
# @Software: PyCharm

'''
定义一个函数，获取两个数里的较大值
'''
def get_max(a,b):
    v=a
    if b>a:
        v=b
    return v
    print("hello")
    # print(v)
i=get_max(25,20)
print(i)

def set_age(age):
    if type(age) !=int:
        return
    if age<0:
        return None
    print(age)
set_age(-3)