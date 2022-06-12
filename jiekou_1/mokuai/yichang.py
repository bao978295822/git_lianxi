# try:
#     print("读")
#     f=open("ceshi.py","r")
#     f.readline()
# except:
#     print("写")
#     f=open("ceshi.py","w")



#1
# try:
#     # print(n)
#     print(1/0)
# except (ZeroDivisionError):
#     print("有错误")

#2
# try:
#     # print(n)
#     print(1 / 0)
# except NameError:
#     print("变量没有定义")
# except ZeroDivisionError:
#     print('不能作为除数')

# try:
#     # print(n)
#     print(1/0)
# except (ZeroDivisionError) as msg:
#     print(f"有错误:{msg}")

# try:
#     print("n")
#     # print(1/0)
# except Exception as msg:
#     print(f"有错误:{msg}")
# else:
#     print("其他情况")
# finally:
#     print("有没有都要执行")

#try内层嵌套
# try:
#     print("一些代码")
#     try:
#         print(n)
#     except FileNotFoundError:
#         print("有错误")
#
# except Exception as msg:
#     print(f"{msg}")


# class xinError(Exception):

class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len
 # 设置抛出异常的描述信息
    def __str__(self):
        return f'你输⼊的⻓度是{self.length}, 不能少于{self.min_len}个字符'
def main():
    try:
        con = input('请输⼊密码：')
        if len(con) < 3:
            raise ShortInputError(len(con), 3)
    except Exception as result:
        print(result)
    else:
        print('密码已经输⼊完成')
main()