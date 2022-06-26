import unittest
# import ddt
from ddt import ddt, data, unpack

list1 = [{"value1":1,"value2":1},{"value1":1,"value2":10111}]


# 创建一个测试类
@ddt
class myTest(unittest.TestCase):
    @data({"value1":1,"value2":1})
    @unpack
    def test_bb1(self, value1, value2):
        self.assertEqual(value1, value2, "数值不等")

    @data({"value1":1,"value2":1},{"value1":3,"value2":1})
    @unpack
    def test_bb2(self, value1, value2):
        self.assertEqual(value1, value2, "数值不等")

    @data(*list1)
    @unpack
    def test_bb3(self, value1, value2):
        self.assertEqual(value1, value2, "数值不等")


if __name__ == '__main__':
    unittest.main(verbosity=2)
