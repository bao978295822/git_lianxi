class Xiyiji(object):
    def __init__(self, w, h):
        self.weight = w
        self.height = h

    def wash(self):
        print(self)
        print("洗衣服")

    def info(self):
        print(f"宽度是{self.weight}")
        print(f"宽度是{self.height}")

# 创建对象
haier1 = Xiyiji(10, 10)
haier1.info()

haier2 = Xiyiji(100, 200)
haier2.info()


class Washer:
    def __str__(self):
        return "我是海尔洗衣机"
    def __del__(self):
        print("我被del了")

haier11=Washer()
print(haier11)

del haier11