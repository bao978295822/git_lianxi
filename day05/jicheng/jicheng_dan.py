class shifu():
    def __init__(self):
        self.peifang="煎饼果子配方"
    def make_cake(self):
        print(f"运用{self.peifang}制作了煎饼")
class zilei(shifu):
    pass
if __name__ == '__main__':
    xiaoming = zilei()
    print(xiaoming.peifang)
    xiaoming.make_cake()


