#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/1 16:48
# @Author : bao
# @Site : 
# @File : zuoye3副本.py
# @Software: PyCharm
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/30 21:58
# @Author : bao
# @Site :
# @File : zuoye3.py
# @Software: PyCharm
'''
1.使用列表推导式生成能被5整除的数（100以内）

'''

#
# def hanshu():
#     list1 = [i for i in range(1, 101) if i % 5 == 0]
#     return list1
#
#
# liebiao = hanshu()
# print(f"第一题：100以内能被5整除的数有：{liebiao}")
'''
2.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
'''
# name=["tom","ceshi","xiaoming","ceshi22"]
# age=[20,19,27,18]
# set1={}
# for i in range(len(name)):
#     set1[name[i]]=age[i]
# print(set1)


'''
3.开发一个注册系统，
页面：
[{name:xxx,age:xxx},{name:xxx,age:xxx},{name:xxx,age:xxx}]
----------------
*   1-新增用户
*   2-查询单个用户
*   3-查询全部用户
*   4-删除用户
----------------
功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
功能2：查询学生信息
功能3：删除学生信息
'''

# def add(name,age):
#     dict1 = {name: name,age:age}
# set2={}
# set2[]
def hanshu3():
    while True:
        print("----------------")
        print("*   1-新增用户")
        print("*   2-查询单个用户")
        print("*   3-查询全部用户")
        print("*   4-删除用户")
hanshu3()