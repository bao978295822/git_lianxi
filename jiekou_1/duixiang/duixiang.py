class Xiyiji(object):
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

haier2=Xiyiji()
print("haier2",haier2)
haier2.wash()

haier1.weight=900
haier1.height=1200
# print(f"宽度是{haier1.weight}")
# print(f"宽度是{haier1.height}")
haier1.info()
