#运用super 自动寻找父类
#师傅类
class shifu:
    def __init__(self):
        self.tiaoliao="五香煎饼（师傅）"
    def make_cake(self):
        print(f"制作了{self.tiaoliao}")
#学校类继承师傅类
class school(shifu):
    def __init__(self):
        self.tiaoliao="香辣煎饼（学校的）"
    def make_cake(self):
        print(f"制作了{self.tiaoliao}")
        super().__init__()
        super().make_cake()

class tudi(school):
    def __init__(self):
        self.tiaoliao="徒弟做的煎饼"
    def make_cake(self):
        print(f"制作了{self.tiaoliao}")

        super().__init__()
        # super.make_cake()
    #子类调用父类方法
    def make_shifu(self):
        shifu.__init__(self)
        shifu.make_cake(self)
    def make_school(self):
        school.__init__(self)
        school.make_cake(self)
    def make_oldcake(self):
        super().__init__()
        super().make_cake()
#实例化
xiaoming=tudi()
#测试推送


xiaoming.make_oldcake()