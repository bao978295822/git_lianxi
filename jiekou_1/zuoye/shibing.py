'''
4.士兵开枪
    需求：
    1）.士兵瑞恩有一把AK47
    2）.士兵可以开火(士兵开火扣动的是扳机)
    3）.枪 能够 发射子弹(把子弹发射出去)
    4）.枪 能够 装填子弹 --增加子弹的数量
类 人类，枪类
人类属性：姓名，有的枪
人类方法：开火
枪的属性    子弹，数量
枪的方法：发射子弹   装填子弹
'''
#定义人类
class ren():
    def __init__(self,name,qiang):
        self.name=name
        self.qiang=qiang
    def fire(self,qiang):
        qiang.fashe()
    def add(self,qiang,one_num):
        qiang.zhuang(one_num)

    #魔法输出
    def __str__(self):
        return f"子弹装了,子弹夹中有{qiang.num}个子弹"
#定义枪类
class qiang():
    def __init__(self):
        self.num=0

    #装填子弹
    def zhuang(self,one_num):
        self.one_num=one_num
        self.num+=one_num

    #发射子弹
    def fashe(self):
        self.num-=1
    #输出
    # def __str__(self):
    #     return f"子弹装了,子弹夹中有{self.num}个子弹"

ak=qiang()
# ak.zhuang(5)
# print(ak)
# ak.fashe()
# print(ak)
#要通过人去调用枪的方法
ruien=ren("ruien","ak")
# ruien.qiang.zhuang(10)
ruien.add(ak,5)
print(f"总的子弹数{str(ak.num)}个")
ruien.fire(ak)
print(f"剩余的子弹数{str(ak.num)}个")
ruien.add(ak,5)
print(f"总的子弹数{str(ak.num)}个")