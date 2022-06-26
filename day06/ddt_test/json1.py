import unittest

# import requests
from ddt import ddt,data ,file_data
@ddt
class myetst(unittest.TestCase):
    @file_data("data.json")
    def test_json1(self,value):
        print(value)
        print(type(value))

if __name__ == '__main__':
    unittest.main(verbosity=2)
