'''
3.列表[1,2,3,4,5,5,2,3,2,4]	去重，不能使用现有函数（10分）
'''
list1 = [1, 2, 3, 4, 5, 5, 2, 3, 2, 4]
list2 = []
for i in list1:
    # print(i)
    if i in list2:
        continue
    else:
        list2.append(i)

print(list2)
'''
4.比如有这样一个文件data.txt内存在以下内容（每行采用逗号分隔）（15分）
----------------------------
lucy:21，tom:30
xiaoming:18，xiaohong:15
xiaowang:20，xiaohei:19
----------------------------
请通过代码读取文件并输出年龄大于18岁的人名
'''


'''
5.请用列表推导式得出1-100能被3整除的数（5分）
'''
list2 = [i for i in range(1, 101) if i % 3 == 0]
print(list2)

'''
7、有一堆字符串，“welocme to super&Test”，打印出emcolew ot  tseT&repus……全部单词原位置反转，
不能使用索引倒序输出或者通过其他现有函数实现，自己写字符串首尾交换方法
'''
str1="welocme to super&Test"
list3=list(str1)
# print(list3)
list4=[]
for i in range(len(list3)):
    list4.append(list3[len(list3)-i -1])
str2=''.join(list4)
# print(str2)
str3=str2.split(" ")
# print(str3)
list5=[]
for i in range(len(str3)):
    # print(i)
    list5.append(str3[len(str3)-i-1])
# print(list5)
# str4="".join(list5)
# print(str4)
for j in range(len(list5)):
    print(list5[j],end='\t')

print("")
'''
10、递归实现斐波那契数列
'''
def digui1(n):
    if n<=1:
        return n
    else:
        return(digui1(n-1)+digui1(n-2))
n1=int(input("请输入数量："))
for i in range(n1):
    print(digui1(i),end=",")
print("")

'''
12、如何实现[‘1’,’2’,’3’]变成[1,2,3] ?
'''
list7=['1','2','3']
list8=[]
for i in list7:
    list8.append(int(i))
print(list8)

'''
13、开发一个注册系统，界面可以用print打印，保存用户名和密码，存在的用户提示已注册，不存在的可以注册成功
（提示建议使用函数划分不同的功能，比如查询用户，新增用户）

'''

new_list=[{"name":"tom","pwd":"123456"}]
def zhuce(**kwargs):
    name,pwd=kwargs
    for i in range(len(new_list)):
        if kwargs[name]==new_list[i]["name"]:
            print("该用户名已存在")
            break
        else:
            new_list.append(kwargs)
            print("注册成功了")
            print(new_list)

# 查询单个用户
def select_one(name):
    for i in range(len(new_list)):
        if name == new_list[i]["name"]:
            print(new_list[i])
        # else:
        #     print("你输入的用户名不存在")

def rukou():
    while True:
        print("*"*20)
        print("1、注册用户")
        print("2、查询你的用户信息")
        print("*"*20)
        n=int(input("请输入你要的功能："))
        if n==1:
            name=input("请输入你的用户名：")
            pwd=input("请输入你的密码：")
            zhuce(name=name,pwd=pwd)
        if n==2:
            name=input("请输入你的用户名：")
            select_one(name)

rukou()