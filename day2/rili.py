#!/usr/bin/python3
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/20 23:06
# @Author : bao
# @Site : 
# @File : rili.py
# @Software: PyCharm
'''
需求：根据用户输入的年月，显示输入月份的日历
'''


def xingqi(y, m, d):
    # 当遇到1，2月的时候，年份建议，月份再12上面加一
    w = (d + 2 * m + 3 * (m + 1) // 5 + y + y // 4 - y // 100 + y // 400) % 7 + 1
    return w


# 闰年1 能被400整除
# 2或者  能被4整除 且不能被100整除的
def runnian(y):
    if y // 400 == 0 or (y // 4 == 0 and y // 100 != 0):
        return True
    return False


while True:
    # 用户分别输入年和月
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    # year=2022
    # month=5
    # 要判断这个月有多少天 28，30，31
    days = 0
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month in [4, 6, 9, 11]:
        days = 30
    elif month == runnian(year):
        days = 29
    else:
        days = 28
    print("""
w1  w2  w3  w4  w5  w6  w7""")
    for i in range(1, days + 1):
        w = xingqi(year, month, i)
        if i == 1:
            print(f"{' ' * (w - 1) * 4}", end="")
        print(i, end="\t")
        if w == 7:
            print("")
    print("")
    # i=xingqi(2021,14,4)
    # print(i)
