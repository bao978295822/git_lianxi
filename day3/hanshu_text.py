#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/30 21:05
# @Author : bao
# @Site : 
# @File : hanshu_text.py
# @Software: PyCharm
'''

定义一个函数
对函数调用
'''
# def hanshu1(i):
#     return i
# shuchu=hanshu1(10)
# print(shuchu)

'''
传入两个数。用函数对这两个数进行相加
'''
def sum1(a,b):
    c=a+b
    return c

he=sum1(5,9)
print(he)

#返回多个值，用多个变量接收
def hanshu2(i,j):
    return i,j

ii,jj=hanshu2(6,9)
print(ii,jj)


'''
atm取钱，先封装一个函数：取钱的界面

'''
