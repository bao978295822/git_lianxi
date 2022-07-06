# 把两个列表组合成字典
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# 方式一：字典 运用推导式的方式

dict = {list1[i]: list2[i] for i in range(len(list1))}
print(dict)

# 方式二：运用普通的for循环
dict1 = {}
for i in range(len(list1)):
    dict1[list1[i]] = list2[i]
print(dict1)
