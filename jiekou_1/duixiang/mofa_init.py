class Xiyiji(object):
    def __init__(self):
        self.weight = 900
        self.height = 1200
    def wash(self):
        print(self)
        print("洗衣服")
    def info(self):
        print(f"宽度是{self.weight}")
        print(f"宽度是{self.height}")

#创建对象
haier1=Xiyiji()
print('haier1',haier1)
haier1.wash()

haier1.info()
