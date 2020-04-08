# -*- coding: utf-8 -*-
# _author_="qqx"
import unittest
import os

# 待执行用例的目录
def allcase():
    case_dir = r"G:\pythonWorkSpace\lebbay\common"
    # case_path=os.path.join(os.getcwd(),"case")
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    # print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到testcase
            print(test_case)
            testcase.addTest(test_case)
    return testcase


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(allcase())

