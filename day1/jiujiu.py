#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/18 21:45
# @Author : bao
# @Site : 
# @File : jiujiu.py
# @Software: PyCharm

'''

写一个九九乘法表
'''

line=1
while line<10:
    shu=1
    while shu<line+1:
        print(f"{shu} * {line} = {line*shu}",end="\t")
        shu+=1
    line+=1
    print("")