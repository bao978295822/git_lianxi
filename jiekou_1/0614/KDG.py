'''
需求主线：
1. 被烤的时间和对应的地⽠状态：
0-3分钟：⽣的
3-5分钟：半⽣不熟
5-8分钟：熟的
超过8分钟：烤糊了
2. 添加的调料：
⽤户可以按⾃⼰的意愿添加调料
类：地瓜类
属性  被烤时间，总的时间，地瓜状态，调料，调料列表
方法：被烤，添加调料
'''


# 类：地瓜类
class kdg():
    # 一开始就有的属性
    def __init__(self):
        self.time = 0
        self.zhuangtai = "生的"
        self.liebiao_tl = []

    # 被烤的状态变化
    def kao(self, one_time):
        self.time += one_time
        if self.time >= 0 and self.time < 3:
            self.zhuangtai = "生的"
        elif self.time >= 3 and self.time < 5:
            self.zhuangtai = "半生不熟"
        elif self.time >= 5 and self.time < 8:
            self.zhuangtai = "熟了"
        elif self.time >= 8:
            self.zhuangtai = "糊了"
        else:
            print("你输入的数据不合法！！")

    # 往地瓜里添加调料
    def add(self, tiaoliao):
        self.liebiao_tl.append(tiaoliao)

    # 定义魔法输出方法
    def __str__(self):
        return f"地瓜烤了{self.time}分钟，现在的状态是{self.zhuangtai},添加的调料有{self.liebiao_tl}"


digua = kdg()
digua.kao(2)
print(digua)
digua.kao(2)
print(digua)
digua.kao(3)
print(digua)
digua.kao(3)
print(digua)
digua.add("黑胡椒")
print(digua)
digua.add("辣椒")
print(digua)
