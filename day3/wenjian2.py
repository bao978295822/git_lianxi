# f=open("aaa.txt","w")     #写入的时候，指针在最前面，覆盖原来的内容  w  如果没有这个文件会创建一个新的文件
f=open("aaa.txt","r")       #也是写入，指针在最后面，在结果添加内容，  文件不存在，创建新文件
# f.write("hello world!!!!")

content=f.read(20)
print(content)
content2=f.readline()
print(content2)
# content1=f.readlines()

# print(content1)

f.close()           #文件操作了，记得关闭






