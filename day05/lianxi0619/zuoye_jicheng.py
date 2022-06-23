# 本节主要练习继承
# 徒弟继承师傅的方法

class shifu():
    def __init__(self):
        self.tiaoliao = "五香煎饼"

    def makeCake(self):
        print(f"制作了{self.tiaoliao}")


# 徒弟继承父类
class tudi(shifu):
    pass


# 实例化一个徒弟
xiaoming = tudi()
xiaoming.makeCake()
