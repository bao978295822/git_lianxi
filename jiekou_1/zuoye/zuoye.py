'''
1、打印小猫爱吃鱼，小猫要喝水
	定义猫类
'''

class mao():
    def chiyu(self):
        print("小猫爱吃鱼")

    def heshui(self):
        print("小猫要喝水")

mao1 = mao()    #实例化一个猫
mao1.chiyu()
mao1.heshui()

'''
2、小明爱跑步，爱吃东西。
    1）小明体重75.0公斤
    2）每次跑步会减肥0.5公斤
    3）每次吃东西体重会增加1公斤
    4）小美的体重是45.0公斤

类：人类
属性 体重，
方法：跑步，吃东西
'''
class renlei():
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
        # print(f"体重为{self.weight}公斤")

    def pao(self):
        self.weight-=0.5
        # self.name=name

        # print(f"体重为{self.weight}公斤")
    def chi(self):
        self.weight+=1
        # self.name=name
        # print(f"体重为{self.weight}公斤")
    def __str__(self):
        return f"名字是{self.name},体重是{self.weight}公斤"

xiaoming=renlei("小明",75.0)       #在这传入参数
# zhong=xiaoming.weight
# print(f"小明体重{zhong}公斤")

xiaoming.pao()
print(xiaoming)
xiaoming.chi()
print(xiaoming)
xiaoming.chi()
print(xiaoming)

xiaomei=renlei("小美",45.0)
print(xiaomei)

'''
3、摆放家具
    需求：
    1）.房子有户型，总面积和家具名称列表
       新房子没有任何的家具
    2）.家具有名字和占地面积，其中
       床：占4平米
       衣柜：占2平面
       餐桌：占1.5平米
    3）.将以上三件家具添加到房子中
    4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
    
类：家具   房子
家具的属性 名字，占地面积
家具的方法   添加

房子的属性   名字，占地面积，家具列表，剩余面积
房子的方法   添加
'''
class jiaju():
    def __init__(self,name,mianji):
        self.name=name
        self.mianji=mianji
        # self.yigui=yigui
        # self.canzhuo=canzhuo
    # def add1(self):

class fangzi():
    liebiao=[]
    # sheng_area=
    def __init__(self,huxing,mianji):
        self.huxing=huxing
        self.mianji=mianji
    def add1(self,jiaju1):
        self.sheng_area=self.mianji-jiaju1.mianji
        if self.sheng_area>jiaju1.mianji:
            self.liebiao.append(jiaju1.name)
        else:
            print("房子里装不下家具了")
    def __str__(self):          #用一个魔法方法，输出
        return f"房子的户型是{self.huxing},总面积是{self.mianji},房子里的家具有{self.liebiao}，剩余的面积是{self.sheng_area}"

chuang=jiaju("床",4)
yigui=jiaju("衣柜",2)
canzhuo=jiaju("餐桌",40)

fang=fangzi("豪宅",30)
# fang.add1(chuang)
fang.add1(chuang)
print(fang)
fang.add1(yigui)
print(fang)
fang.add1(canzhuo)
print(fang)