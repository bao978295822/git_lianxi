# 练习变量

name = 'bao'
print(name)
print(id(name))
SchoolName = "海滨学院"
print(SchoolName)

# 数据类型
# 整型int
int1 = 23
print(type(int1))

# 整型float
f1 = 2.444
print(type(f1))

# 布尔类型
bool1 = True
print(type(bool1))

# 字符串类型
str1 = '123'
print(type(str1))

# 列表
list1 = [1, 2, 3]
print(type(list1))

# 元组
tup1 = (1, 2, 3)
print(type(tup1))

# 集合
set1 = {1, 2, 3}
print(type(set1))

# 字典类型
dict1 = {1: 1}
print(type(dict1))

# 输出我的名字是宝，体重是75.5kg
name1 = "宝"
weight = 75.50
print("我的名字是%s,体重是%.2fkg" % (name1, weight))

# 运用f表达式
print(f"我的名字是{name1},体重是{weight}kg")

print(123,end='\t')
print(123)


#输入
# name2=input("请输入你的姓名：")
# print("你的姓名是%s"%name2)
#
# pwd=int(input("请输入你的密码"))
# print(pwd)


#数据类型转换 eval
list2='{1,2,3}'
ev1=eval(list2)
print(ev1)
print(type(ev1))

#int类型转换为flocat类型
int2=45
f2=float(int2)
print(type(f2))

#列表转换为元组
list3=[1,2,3,4]
tup2=tuple(list3)
print(type(tup2))
print(tup2)

tup3=(1,3,4,5)
list4=list(tup3)
print(list4)