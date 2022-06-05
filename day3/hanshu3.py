'''
os包
'''
import os
#文件重命名
# os.rename("bb.txt","aa.txt")     #文件重命名

# os.remove("bb2.txt")  #删除文件
# os.mkdir("ceshi") #创建文件夹
# os.rmdir("ceshi") 删除文件夹

print(os.getcwd())  #获取当前目录位置
print(os.listdir()) #获取当前文件目录的文件
#
print(os.path.dirname(__file__))