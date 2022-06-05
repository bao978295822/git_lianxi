# def hanshu():
#     aa=100
#     print(aa)
# hanshu()
# print(aa)

# a = 100
# def hanshu1():
#     # global a
#     a = 20
#     print(a)
#     print(id(a))
#
#
# def hanshu2():
#     print(a * a)
# hanshu1()
# hanshu2()
# print(id(a))
#
# def fun1():
#     return [1,2,43,4,43]
#     return 2000
# def fun2(n):
#     print(n)
# num =fun1()
# fun2(num)
# print(type(fun1()))

# def user_info(name,age,gender,coutury="中国"):
#     print(f"你的名字是{name},你的年龄是{age},你的性别是{gender}，你的国籍是{coutury}")
#     # print("你的名字是%s"%name)
# user_info("tom",22,"男")
#
# user_info("小明",gender="女",age=15,coutury="美国")
# print()


# def fun1(*args):
#     print(args)
#
# fun1("ceshi",18,33)
# # print(fun1())
# user_msg=["ceshi",18,22]
# # print(*user_msg)
# fun1(*user_msg)


# def user_info(**kwargs):
#     print(kwargs)
#
# user_info(name="ceshi",age=20)
# # user_info(**"ceshi",18,90)
# user_msg={"name":"ceshi","age":20}
# user_info(**user_msg)

'''
进行拆包
'''
# def hanshu1():
#     return 100,200
# a,b=hanshu1()
# print(a)
# print(b)

# dict1={"a":1,"age":20}
# a,b=dict1.items()
# print(a)
# print(b)
#
#
# '''
# 两个数互换值
# '''
# a=100
# b=200
# a,b=b,a
# print(a)
# print(b)


