class shifu():
    def __init__(self):
        self.peifang = "煎饼果子配方"
        self.__money = 300

    def make_cake(self):
        print(f"运用{self.peifang}制作了煎饼")

    def __siyou(self):
        print(self.__money)

    def get_money(self):
        print(self.__money)

    def set_monry(self, n):
        if n > 0:
            self.__money += n
            print(self.__money)
        else:
            print("不要偷拿钱")


class zilei(shifu):
    pass


if __name__ == '__main__':
    xiaoming = zilei()
    # print(xiaoming.__money)
    # xiaoming.__siyou()
    shifu1 = shifu()
    # shifu1.__siyou
    xiaoming.get_money()
    xiaoming.set_monry(300)
    # print(xiaoming)
    xiaoming.set_monry(-100)
