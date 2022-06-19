class shifu():
    def __init__(self):
        self.peifang = "五香煎饼果子配方"

    def make_cake(self):
        print(f"运用{self.peifang}制作了煎饼")


class school():
    def __init__(self):
        self.peifang = "香辣煎饼果子"

    def make_cake(self):
        print(f"运用{self.peifang}制作了煎饼")


class zilei(shifu, school):
    def __init__(self):
        self.peifang = "独创煎饼果子"

    def make_cake(self):
        self.__init__()

        print(f"运用{self.peifang}制作了煎饼")

    def make_shifu_cake(self):
        shifu.__init__(self)
        shifu.make_cake(self)
        # print(f"运用{self.peifang}制作了煎饼")

    # 制作学校的
    def make_school_cake(self):
        school.__init__(self)
        school.make_cake(self)

    def make_old_cake(self):
        # 方法一，指名道姓调用
        # shifu.__init__(self)
        # shifu.make_cake(self)
        # 方法二，运用super
        # 2.1
        # super().__init__()
        # super().make_cake()
        # 方法2。1
        super(zilei, self).__init__()
        super(zilei, self).make_cake()


# 创建徒孙类
class tusun(zilei):
    pass


if __name__ == '__main__':
    # xiaoming = zilei()
    # xiaoming.make_old_cake()
    # xiaoming.
    sunzi = tusun()
    print(sunzi.peifang)
    sunzi.make_cake()
    sunzi.make_school_cake()
