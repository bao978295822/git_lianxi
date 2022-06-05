#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/20 14:56
# @Author : bao
# @Site : 
# @File : list1.py
# @Software: PyCharm
#
# list1=["bao","weijia","dupeng"]
# name=input("请输入姓名查询是否存在：")
# if name in list1:
#     print(f"你输入的姓名是{name},姓名存在列表中")
# else:
#     print(f"你输入的姓名是{name}，姓名不存在")
#
# list2=["bao","weijia","dupeng"]
# list2.append("cc")
# print(list2)
# list3=["bao","weijia","dupeng"]
# for i in list3:
#     print(i)


list2=["tom","lily","bao","tom"]
# print(list2[0])
# print(list2[1])
# print(list2.index("tom"))
# # print(list2.index("bao1"))
# print(list2.count("tom"))
# print(len(list2))
# name=input("请输入名字，查看是否存在:")
# if name in list2:
#     print(f"你输入得名字是{name},存在列表中")
# # else:
# #     print(f"你输入得名字是{name},不存在列表中")
# if name not in list2:
#     print(f"你输入得名字是{name},不存在列表中")

# list3=["tom","bao","weijia"]
# list3.append("babao")
# print(list3)
# list3.extend("aaa")
# print(list3)
# aa=["ceshi","ceshi"]
# list3.extend(aa)
# print(list3)
# list3.insert(2,"laile")
# print(list3)

# list4=["tom","bao","weijia"]
# del list4

# print(list4)

# del list4[0]
# print(list4)

# print(list4.pop(0))
# print(list4)

# list4.remove("tom")
# print(list4)
#
# list4.clear()
# print(list4)

# list5=["tom","bao","weijia"]
# list5[0]="hahaha"
# print(list5)


# list6.reverse()
# print(list6)
# new_list=reversed(list6)
# print(new_list)
# print(list(new_list))
# print(list6)

#sort
# list6.sort(reverse=True)
# print(list6)
# list6=[1,7,5,3,2]
# list7=sorted(list6,reverse=True)
# print(list7)


#while循环
# name_list=["ceshi","tom","babao","weijia"]
# # i=0
# # while i<len(name_list):
# #     print(name_list[i])
# #     i+=1
#
# j=0
# for j in name_list:
#     print(j)

list1=[["ceshi","babao","weijia"],["tom","jerry"],["hello","world","bao"]]
print(list1[0])
print(list1[1][1])

#死循环得应用
while True:
    print("""1、新增
    2、修改
    3、删除
    4、退出系统
    """)
    a=int(input("请选择你要使用得功能："))
    if a==1:
        print("新增成功")

    elif a==4:
        print("退出系统")
        break

#将8个老师随机分配到三个教室
