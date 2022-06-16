#这一节主要是练习导模块和导包
#导入自己写的包
from jiekou_1.a0616.baoa import hanshu

hanshu.jian(8, 3)

print("*"*30)
# from mokuai.bao.model
import math
print(math.sqrt(9))

from math import sqrt

print(sqrt(14))

from math import sqrt as sq

print(sq(25))

