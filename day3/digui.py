def fun(n):
    if n==1:
        return 1
    return n+fun(n-1)

nn=fun(5)
print(nn)