import unittest
from ddt import ddt, data, unpack
list1=[1,3,4]

@ddt
class test_ceshi(unittest.TestCase):

    @data(1)
    def test_a(self, value):
        print(value)
        # unittest.TestCase.assertEqual(value, 2)
        self.assertEqual(value,1)
    @data(1,2)
    def test_b(self,value):
        print(value)
        self.assertEqual(value,2)
    @data(*list1)
    def test_c(self,value):
        self.assertEqual(value,3)

if __name__ == '__main__':
    unittest.main(verbosity=2)
