#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/20 20:38
# @Author : bao
# @Site : 
# @File : hanshu.py
# @Software: PyCharm

'''
写一个函数
然后对这个函数进行调用
'''


def hanshu():
    print("这是一个函数")

def good_morning():
    hanshu()
    print("Good morning")

good_morning()

def line(i,char):
    '''
    测试函数显示自定义文档

    :param i:
    :param char:
    :return:
    '''
    print(char * i)
line
