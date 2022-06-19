"""
士兵开枪
两个类：枪类 士兵类
枪类（Gun）:
属性：型号（model），弹夹中⼦弹的数⽬（bullet_count）
方法：射击⼦弹（shoot），添加⼦弹（add_bullet）
⼠兵类（soldier）：
（1）属性：姓名（name），枪名（Gun）
（2）⽅法：开⽕（shoot）

"""
class Gun():
    # 属性：型号（model），弹夹中⼦弹的数⽬（bullet_count）
    def __init__(self,model,bullet_count):
        self.model=model
        self.bullet_count=bullet_count

        # 方法：射击⼦弹（shoot）
    def shoot(self):
        if self.bullet_count==0:
             print("没有子弹了")
        else:
            self.bullet_count-=1
            print("已经射中了")

        #方法：添加⼦弹（add_bullet）
    def add_bullet(self,zidanshu):
        self.bullet_count+=zidanshu

    def __str__(self):
        return f'枪型是{self.model}里面有{self.bullet_count}颗子弹'

class Soldier():
    #士兵姓名
    def __init__(self, name):
        self.name = name

    # 射击
    def shoot(self, item):
        item.shoot()


    # 装子弹
    def add_bullet(self, item, zidanshu):
        item.add_bullet(zidanshu)

    def __str__(self):
        return f"士兵的姓名是：{self.name}"

if __name__ == '__main__':
    gun=Gun("ak",1)
    print(gun)

    soldier=Soldier("瑞恩")
    print(soldier)

    soldier.shoot(gun)
    soldier.shoot(gun)

    print("*"*30)

    #装填子弹
    soldier.add_bullet(gun,2)

    #查看是否填充
    print(gun)

    print(soldier)
    #射光
    soldier.shoot(gun)
    soldier.shoot(gun)
    soldier.shoot(gun)



