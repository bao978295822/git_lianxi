#定义两个函数，一个加法，一个减法
def jia(a,b):
    print(a+b)
def jian(a,b):
    print(a-b)

#为了防止自己测试调用的方法，出现在别的地方，影响结果，使用main函数
if __name__ == '__main__':
    jia(5,6)
    jian(9,6)