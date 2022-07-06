'''
#1、需求：有三个办公室，8位⽼师，8位⽼师随机分配到3个办公室
#用到了随机函数
办公室 list1
老师 list2

'''
# import random
from random import randint

#
# 办公室   把老师分配到这个内嵌的列表中
list1 = [[], [], []]
# 老师
teac = [1, 2, 3, 4, 5, 6, 7, 8]

for name in teac:
    # print(name) #遍历所有老师
    # index=randint(0,2)
    # list1[index].append(name)
    list1[randint(0, 2)].append(name)
print(list1)
