#主要是理解深浅拷贝

import copy
a=100
b=a
print(id(a))
print(id(b))
a=300
print(id(a))
print(id(b))
print(a)
print(b)

list1=[1,2,[3,4,5]]
# list2=copy.deepcopy(list1)#深拷贝
list2=list1.copy()        #浅拷贝
print(id(list1))
print(id(list2))
# list1[1]="ceshi"
print(list1)
print(list2)
list1[2][1]=222
print(list1)
print(list2)
print(id(list1[2]))
print(id(list2[2]))

list3=[1,2,3,[4,5,6]]
list4=copy.deepcopy(list3)
print(id(list3))
print(id(list4))
list3[3][1]=777
print(list3)
print(list4)
print(id(list3[3][1]))
print(id(list4[3][1]))