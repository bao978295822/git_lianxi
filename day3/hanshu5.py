def fun1(n):
    return n ** 2


list1 = [1, 2, 3, 4, 5]
res = map(fun1, list1)
print(res)
res = list(res)
print(res)

import functools

list1 = [1, 2, 3, 4, 5, 6]


def fun2(a, b):
    return a + b


res1 = functools.reduce(fun2, list1)
print(res1)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def fun3(x):
    return x % 2 == 0


result = filter(fun3, list2)
print(result)
result = list(result)
print(result)
