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


class zilei(school, shifu):
    def __init__(self):
        self.peifang = "独创煎饼果子"

    def make_cake(self):
        self.__init__()

        print(f"运用{self.peifang}制作了煎饼")

    def make_shifu_cake(self):
        shifu.__init__(self)
        shifu.make_cake(self)
        # print(f"运用{self.peifang}制作了煎饼")

    #制作学校的
    def make_school_cake(self):
        school.__init__(self)
        school.make_cake(self)

if __name__ == '__main__':
    xiaoming = zilei()

    xiaoming.make_shifu_cake()
    xiaoming.make_cake()
    xiaoming.make_school_cake()