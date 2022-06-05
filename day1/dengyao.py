#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/17 22:08
# @Author : bao
# @Site : 
# @File : dengyao.py
# @Software: PyCharm

# # 4.打印等腰三角形
line = 5    #行数
i = 1   #定义循环的一个变量
while i <= line:    #当行数大于6的时候就不打印了
    j = 1   #空格数
    while j < line - i:  #
        print(" ", end="")
        j += 1
    k = 1   #代表星星数
    # while k < i + 1:  #右对齐的三角形
    while k < 2*i - 1:  #等腰三角形
        print("*", end="")
        k += 1
    print("")
    i += 1