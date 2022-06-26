import unittest
# import ddt
from ddt import ddt, data,unpack
list1=[1,2,23,3]

# 创建一个测试类
@ddt
class myTest(unittest.TestCase):
    @data(1)
    def test_bb1(self, value):
        self.assertEqual(value, 1, "数值不等")
    @data(1,2,3)
    def test_bb2(self,value):
        self.assertEqual(value,2,"数值不等")
    @data(*list1)
    def test_bb3(self,value):
        self.assertEqual(value,2,"shuzhibudeng")

if __name__ == '__main__':
    unittest.main(verbosity=2)
