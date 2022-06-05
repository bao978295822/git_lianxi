# 主要是联系map方法的使用

#定义一个函数
def fun1(i):
    return i*i

list1=[1,3,5,6,7,8,9,100]

shuchu=map(fun1,list1)
print(shuchu)   #输出的是一个对象
print(list(shuchu))