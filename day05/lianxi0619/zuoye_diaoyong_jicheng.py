# 本节主要练习  同时吃到师傅和学校做的煎饼
# 徒弟继承师傅的方法

class shifu():
    def __init__(self):
        self.tiaoliao = "五香煎饼"

    def makeCake(self):
        print(f"制作了{self.tiaoliao}")
class school:
    def __init__(self):
        self.tiaoliao="学校煎饼"
    def makeCake(self):
        print(f"制作了{self.tiaoliao}")

# 有多个父类的时候，默认继承第一个父类
class tudi(shifu,school):
    def __init__(self):
       self.tiaoliao="徒弟自制的煎饼果子"
    def makeCake(self):
        self.__init__()
        print(f"制作了{self.tiaoliao}")
    def make_shifu(self):
        shifu.__init__(self)
        shifu.makeCake(self)

# 实例化一个徒弟
xiaoming = tudi()
xiaoming.makeCake()
xiaoming.make_shifu()