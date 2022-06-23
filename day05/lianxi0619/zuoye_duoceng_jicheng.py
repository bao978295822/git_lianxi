# 本节主要练习多继承
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
class tudi(school,shifu):
    def __init__(self):
        self.tiaoliao = "徒弟自制的煎饼果子"

    def makeCake(self):
        self.__init__()
        print(f"制作了{self.tiaoliao}")

    def make_shifu(self):
        shifu.__init__(self)
        shifu.makeCake(self)
    def make_school(self):
        school.__init__(self)
        school.makeCake(self)
class sun(tudi):
    pass


# 实例化一个徒弟
suner=sun()
suner.makeCake()
suner.make_shifu()
suner.make_school()