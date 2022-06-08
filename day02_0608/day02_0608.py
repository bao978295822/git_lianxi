list1 = ["ceshi", "bao", "weijia"]
print("ceshi" in list1)  # 字符串在列表中返回true
print("ceshi1" in list1)

list1.append("tom")
print(list1)

set1 = {1, 2, 3}
list1.extend(set1)  # 把每一个元素插入，可以是列表或者集合
print(list1)

list1.insert(0, "jerry")  # 在第0个位置插入数据
print(list1)

del list1[1]
print(list1)

fanhui = list1.pop(0)  # 删除之后会返回一个数据
print(list1)
print(fanhui)

list1.remove("bao")  # 移除具体的数据
print(list1)

list1[0] = "weijia11111"
print(list1)

list1.reverse()  # 对数据进行逆置
print(list1)

cp_list = list1.copy()
print(cp_list)

for i in list1:
    print(i, end='\t')

print("")
# 元组的常见操作

tup1 = (1, 2, 3, 4, 1, 1, 1)
shu = tup1.count(1)  # 计算某个字符在元组中出现的次数
print(shu)

print(len(tup1))  # 计算长度

# 字典
dict1 = {"name": "tom", "age": 20}
dict1["guojia"] = "zhongguo"  # 没有key则新增，有就修改
print(dict1)
dict1["name"] = "ceshi"
print(dict1)

del dict1["name"]
print(dict1)        #删除

#根据key来查找
print(dict1["age"])

#遍历每个元素
for i in dict1.items():
    print(i)


#遍历key=value
for key,value in dict1.items():
    print(f"{key}={value}")

#练习集合的操作

set2={1,2,3,4,5,1}
print(set2)     #集合去重
set2.add("ceshi")
print(set2)
set2.remove(1)
print(set2)

#range
for i in range(10):
    print(i,end='\t')
print("")


#列表推导式
list2=[i for i in range(10) if i%3==0]
print(list2)

#字典推导式
dict1={i:i*i for i in range(1,10)}
print(dict1)

#把两个列表合并成一个字典
new_list=["name","age","sex"]
new_list2=["ceshi",20,"女"]
dict2={new_list[i]:new_list2[i] for i in range(len(new_list))}
print(dict2)

