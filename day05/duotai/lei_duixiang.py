class dog():
    __ya=10
    #通过cls访问私有属性
    @classmethod
    def info(cls):
        return cls.__ya
    @staticmethod
    def jingtai():
        print("使用了静态方法")

dahuang = dog()
xiaohei = dog()
print(dahuang.info())
xiaohei.jingtai()
dog.jingtai()

