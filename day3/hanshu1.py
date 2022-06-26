'''
函数--不定长参数，可变参数
位置参数
关键字参数
'''


def hanshu(*args):
    print(args)

def hanshu2(**kwargs):
    print(kwargs)

a = "weijia"
hanshu(a)
hanshu(*a)

hanshu("ceshi", 19)
list1 = [19, 23, 23, 56]
hanshu(*list1)  # 传入的时候必须带上*号
dict1={"a":1,"b":33}
hanshu(dict1)
hanshu(*dict1)
hanshu(*dict1.items())

hanshu2(**dict1)
hanshu2(name="ceshi",age=22,sex="男")