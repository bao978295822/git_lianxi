'''
4.士兵开枪
    需求：
    1）.士兵瑞恩有一把AK47
    2）.士兵可以开火(士兵开火扣动的是扳机)
    3）.枪 能够 发射子弹(把子弹发射出去)
    4）.枪 能够 装填子弹 --增加子弹的数量

类：
士兵类 属性  姓名，枪，
士兵类 方法  开火

枪类 属性  名字，子弹数量，子弹剩余数量，
枪类 方法   发射子弹，装填子弹，

'''


class qiang():
    def __init__(self, qiang_name):
        self.qiang_name = qiang_name
        self.num = 0

    def fashe(self):
        # 判断如果子弹数量小于0，不能发射
        if self.num <= 0:
            print("没有子弹了")
        # 反之，子弹数量减一
        else:
            print("发射成功了,子弹数量减一")
            self.num -= 1

    def zhuang(self):
        self.num += 5

    def __str__(self):
        return f"{self.qiang_name}有{self.num}个子弹"


class shibing():
    def __init__(self, name, qiang1):
        self.name = name
        self.qiang1 = qiang1

    def fire(self):
        # ak.fashe
        self.qiang1.fashe()

        # qiang.fashe()
    def zhuang_1(self):
        # ak.zhuang()
        # self.qiang.
        self.qiang1.zhuang()


    def __str__(self):
        return f"{self.name},有{self.qiang1},枪里有{ak.num}个子弹"

if __name__ == '__main__':
    ak = qiang("ak")
    print(ak)
    # ak.fashe()
    # print(ak)
    # ak.zhuang()
    # print(ak)
    # ak.fashe()
    # print(ak)
    ruien = shibing("ruien", ak)
    ruien.fire()
    print(ruien)
    ruien.zhuang_1()
    print(ruien)
    ruien.fire()
    print(ruien)