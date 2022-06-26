import unittest
from myfun import *
class mytest(unittest.TestCase):
    def test_add(self):
        print("执行了加法")
        yuqi=add(1,2)
        self.assertEqual(yuqi,3,"预期结果与实际结果不符合")

    def setUp(self) -> None:
        print("这是用例执行前的工作")
    def tearDown(self) -> None:
        print("用例执行后的清理工作")
    # @unittest.skip("跳过")
    # @unittest.skipIf(1==1,"tiaoguo")
    # @unittest.skipUnless(1==0,"不满足则跳过")
    def test_cheng(self):
        # self.skipTest("未开发完成，跳过")
        print("执行了乘法")
        yuqi=multi(2,6)
        self.assertEqual(yuqi,10,"预期与实际不符合")
    @classmethod
    def setUpClass(cls) -> None:
        print("所有用例执行前的准备工作")
    @classmethod
    def tearDownClass(cls) -> None:
        print("所有用例执行之后的清理工作")


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    #生成测试套件
    suit=unittest.TestSuite()
    suit.addTest(mytest("test_cheng"))
    suit.addTest(mytest("test_add"))
    #执行多个
    # suit.addTests([mytest("test_cheng"),mytest("test_add")])

    run=unittest.TextTestRunner(verbosity=2)

    run.run(suit)