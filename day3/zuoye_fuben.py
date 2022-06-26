
'''
1.使用列表推导式生成能被5整除的数（100以内）

'''


def hanshu():
    list1 = [i for i in range(1, 101) if i % 5 == 0]
    return list1


liebiao = hanshu()
print(f"第一题：100以内能被5整除的数有：{liebiao}")
'''
2.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
'''
name=["tom","ceshi","xiaoming","ceshi22"]
age=[20,19,27,18]
set1={}
for i in range(len(name)):
    set1[name[i]]=age[i]
print(set1)

'''
1.使用列表推导式生成能被5整除的数（100以内）
2.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
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

复习重点:
定义函数
调用函数
传参方式
'''

# 查询
# 请输入你要操作的项
list1 = [{"name": "tom", "age": 20}, {"name": "ceshi", "age": 25}]


def add(**kwargs):  # 新增用户
    a, b = kwargs

    # print(a,b)
    for i in range(len(list1)):
        # print(i)
        if kwargs[a] == list1[i]["name"]:
            print("你输入的用户名已存在列表中")
            break
    else:
        print("新增成功！")
        list1.append(kwargs)


# 查询单个用户
def select_one(name):
    for i in range(len(list1)):
        if name == list1[i]["name"]:
            print(list1[i])


# 查询全部
def select_all():
    for i in range(len(list1)):
        print(list1[i])


# 删除
def del1(name):
    # name=input("请输入你的姓名")
    # print(len(list1))
    for i in range(len(list1)):
        # print(list1[i])
        if name == list1[i]["name"]:
            list1.pop(i)
            # print(list1)
            break
        # else:
        #     print("你输入的姓名不存在")
    print("删除成功！")
    print(list1)


def rukou():
    while True:
        print("-"*20)
        print("1-新增用户")
        print("2-查询单个用户")
        print("3-查询全部用户")
        print("4-删除用户")
        print("-"*20)


        n = int(input("请输入你要选择的功能："))
        if n == 1:
            # print("1")
            name = input("请输入你的姓名：")
            age = int(input("请输入你的年龄："))
            add(name=name, age=age)
            print(list1)
        elif n == 2:
            # print("2")
            name = input("请输入你的名字")
            select_one(name)
        elif n == 3:
            # print("3")
            select_all()
        elif n == 4:
            # print("4")
            name = input("请输入你要删除的姓名：")
            del1(name)
        else:
            print("退出系统")
            break


rukou()

