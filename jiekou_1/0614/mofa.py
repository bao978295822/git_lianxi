#定义与生俱来的属性

class Washer():
    #定义init方法
    def __init__(self):
        self.height=500
        self.wight=300
    # def pri_info(self):
    #     print(f"洗衣机的高度是{self.height},长度是{self.wight}")

    #定义一个魔法的输出方法
    def __str__(self):
        return f"洗衣机的高度是{self.height},长度是{self.wight}"

haier=Washer()
# haier.pri_info(洗衣机的高度是{self.height},长度是{self.wight})

print(haier)
