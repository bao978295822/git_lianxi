class dog():
    ya = 10
    def __init__(self):
        self.age=5
    def info(self):
        print(self.age)


dahuang = dog()
xiaohei = dog()
print(dahuang.ya)
print(xiaohei.ya)
print(dog.ya)

dog.ya=15
dahuang.ya=5
print(dahuang.ya)
print(xiaohei.ya)
print(dog.ya)

dahuang
