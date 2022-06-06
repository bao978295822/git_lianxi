#练习变量

name='bao'
print(name)
print(id(name))
SchoolName="海滨学院"
print(SchoolName)

#数据类型
#整型int
int1=23
print(type(int1))

#整型float
f1=2.444
print(type(f1))

#布尔类型
bool1=True
print(type(bool1))

#字符串类型
str1='123'
print(type(str1))

#列表
list1=[1,2,3]
print(type(list1))

#元组
tup1=(1,2,3)
print(type(tup1))

#集合
set1={1,2,3}
print(type(set1))

#字典类型
dict1={1:1}
print(type(dict1))

#输出我的名字是宝，体重是75.5kg
name1="宝"
weight=75.50
print("我的名字是%s,体重是%.2fkg"%(name1,weight))

#运用f表达式
print(f"我的名字是{name1},体重是{weight}kg")