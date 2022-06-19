class shifu():
    def __init__(self):
        self.peifang="五香煎饼果子配方"
    def make_cake(self):
        print(f"运用{self.peifang}制作了煎饼")

class school():
    def __init__(self):
        self.peifang="香辣煎饼果子"
    def make_cake(self):
        print(f"运用{self.peifang}制作了煎饼")
class zilei(school,shifu):
    def __init__(self):
        self.peifang="独创煎饼果子"
    def make_cake(self):
        print(f"运用{self.peifang}制作了煎饼")
if __name__ == '__main__':
    xiaoming = zilei()
    print(xiaoming.peifang)
    xiaoming.make_cake()


