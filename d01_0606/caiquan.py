# 猜拳的游戏
import random

wanjia = int(input("请输入1石头 2剪刀 3布："))
com = random.randint(0, 2)
# print(com)
# 下面是玩家赢的情况
if wanjia == 1 and com == 2:
    print("玩家胜利")
elif wanjia == 2 and com == 3:
    print("玩家胜利")
elif wanjia == 3 and com == 1:
    print("玩家胜利")
elif wanjia == com:
    print("玩家和电脑打成了平手")
else:
    print("电脑胜利")
