'''
写代码前先理思路

需求主线：
1. 被烤的时间和对应的地⽠状态：
0-3分钟：⽣的
3-5分钟：半⽣不熟
5-8分钟：熟的
超过8分钟：烤糊了
2. 添加的调料：
⽤户可以按⾃⼰的意愿添加调料

类 地瓜类
属性  单次时间，总时间，状态str，调料list
方法  烤地瓜  ， 添加调料

'''

#类遵循标识符的命名规则：1数字字母下划线组成 2不能以数字开头 3不能使用内部关键字

# 遵循大驼峰的命名规则
# 定义一个地瓜类
class KDG():
    # 属性初始化
    def __init__(self):
        self.time = 0
        self.zhuangtai = '生的'
        self.list_tiaoliao = []

    # 烤地瓜的方法
    def kao(self, dan_time):
        self.time += dan_time
        if 0 <= self.time < 3:
            self.zhuangtai = '生的'
        elif 3 <= self.time < 5:
            self.zhuangtai = '半生不熟'
        elif 5 <= self.time < 8:
            self.zhuangtai = '熟的'
        elif self.time >= 8:
            self.zhuangtai = '烤糊了'
        # 限制非法输入
        else:
            print("你输入的时间非法")

    # 添加调料的方法
    def tian_tiaoliao(self, tiaoliao):
        return self.list_tiaoliao.append(tiaoliao)

    # 为了打印结果，定义一个魔法方法
    def __str__(self):
        return f"地瓜烤了{self.time}分钟,地瓜的状态是{self.zhuangtai}，添加的调料有{self.list_tiaoliao}"


# 测试用
if __name__ == '__main__':
    # 实例化
    digua = KDG()
    # digua.kao(-20)
    # print(digua)
    #实例调用方法
    digua.kao(2)
    print(digua)
    digua.kao(1)
    print(digua)
    digua.kao(3)
    print(digua)
    digua.kao(3)
    print(digua)
    digua.tian_tiaoliao("胡椒粉")
    print(digua)
    digua.tian_tiaoliao("辣椒")
    print(digua)
    digua.tian_tiaoliao("孜然")
    print(digua)
