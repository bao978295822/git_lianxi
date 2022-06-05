'''
文件操作  utf-8

r   w  a
'''
f=open('aa.txt','r+',encoding="utf-8")
# print(f)
# f1=open("aa.txt","r",)
# f.write("aaaaa")
#读取文件
res=f.read(6)
print(res)
print(f.read(4))
# print(f.read())
# print(f.readlines())
print(f.readline())

print(f.readline())
print(f.readline())
print(f.readline(5))

# print(f.tell())

# print(f.seek(0,2))
# print(f.readline())
# print(f.tell())

f.seek(5,0)
print(f.tell())
print(f.readline())
print(f.tell())
f.close()

'''
with open这是另一种的写法，这种不用close
'''
with open('aa.txt','r+',encoding="utf-8") as f:
    # 读取文件
    res = f.read(6)
    print(res)
    print(f.read(4))
    # print(f.read())
    # print(f.readlines())
    print(f.readline())

    print(f.readline())
    print(f.readline())
    print(f.readline(5))
    f.seek(5, 0)
    print(f.tell())
    print(f.readline())
    print(f.tell())

