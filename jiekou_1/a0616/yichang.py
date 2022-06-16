# import requests
# r=requests.get("https://www.baidu.com")
# print(r.status_code)
# try:
#     f=open("ceshi.py","r")
# except:
#     print("出错了")
try:
    print(name)
    f = open("ceshi.py", "r")
except(NameError,FileNotFoundError):
    print("文件没有找到")
    print("name变量没有定义")

try:
    print(name)
    f = open("ceshi.py", "r")
except(Exception) as result:  #Exception是所有异常的父类，包含所有的异常  as 起别名
    print("文件没有找到")
    print("name变量没有定义")
    print(result)
try:
    print(1+2)
except Exception as result:
    print(result)
else:
    print("我是没有异常走的逻辑")


