# 将两个列表合成一个字典
list1 = ["name", 20, "男"]
list2 = ["tom", "age", "sex"]
dict1 = {list1[i]: list2[i] for i in range(len(list1))}  #目的是要字典，所以要写字典的格式{list1[i]:list2 for i in rangge(长度)}
print(dict1)
