class dog():
    def work(self):
        print("指哪打哪")

class Adog(dog):
    def work(self):
        print("追击敌人")

class DuGou(dog):
    def work(self):
        print("追击毒品")

class person():
    def work_with_dog(self,dog1):
        dog1.work()

ren=person()
ptg=dog()
adg=Adog()
dg=DuGou()
ren.work_with_dog(ptg)
ren.work_with_dog(adg)
ren.work_with_dog(dg)

