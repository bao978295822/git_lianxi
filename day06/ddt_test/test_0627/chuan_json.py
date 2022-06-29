import unittest
from ddt import ddt,data,unpack,file_data

@ddt
class test_a(unittest.TestCase):
    @file_data("/Users/bao/PycharmProjects/vip_20/day06/ddt_test/test_0627/data.json")
    def test_aa(self,value):
        # self.assertEqual(value,3)
        print(value)

if __name__ == '__main__':
    unittest.main(verbosity=2)