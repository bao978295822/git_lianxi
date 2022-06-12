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
    方法：被烤，添加调料
    属性
    烤的时间，地瓜状态，调料
'''
#定义一个地瓜类
class dihua():  #类里面存放方法和属性
    def __init__(self):     #这些属性定义的时候应该与生俱来
        self.c_time = 0  # 时间初始化为0
        self.tiaoliao = []  # 调料为列表，初始化为空
        self.zhuangtai = '生的'  # 地瓜状态默认是生的
    # time=0  #时间初始化为0
    # tiaoliao=[] #调料为列表，初始化为空
    # zhuangtai='生的'  #地瓜状态默认是生的
    def kao(self,time):     #定义被烤的方法,传入的是单个的时间
        self.c_time+=time
        if 0<self.c_time<=3:
            # print("生的")
            self.zhuangtai="生的"
        elif 3<self.c_time<=5:
            # print("半生不熟")
            self.zhuangtai="半生不熟"
        elif 5<self.c_time<=8:
            # print("半生不熟")
            self.zhuangtai="烤熟了"
        elif self.c_time>8:
            # print("烤熟了")
            self.zhuangtai="烤糊了"
        else:
            print("你输入的数据不合法！")

    def tianjia(self,liao): #添加调料的方法
        self.tiaoliao.append(liao)
    def __str__(self):
        return f"被烤的时间为{self.c_time}分钟,地瓜的状态为{self.zhuangtai},添加的调料有{self.tiaoliao}"

digua1=dihua()  #实例化一个具体的事物，地瓜1
digua1.kao(1)
print(digua1)
digua1.kao(3)
print(digua1)
digua1.kao(2)
print(digua1)
digua1.tianjia("辣椒")
print(digua1)
digua1.tianjia("黑胡椒")
print(digua1)


