from appium import webdriver
import unittest
import HTMLTestRunner
import time
import logging
import os
#测试用例的路径
file_path = "./Project/Test_Case"
def creat_suite():
    #定义测试套
    uit = unittest.TestSuite()
    #测试用例路径
    discover = unittest.defaultTestLoader.discover(file_path, pattern ='test_*.py')
    #添加测试用例到测试套中
    for test_suite in discover:
        for test_case in test_suite:
            uit.addTest(test_case)
    return  uit
suite = creat_suite()
if __name__ == '__main__':
    #生成测试报告
    report_path = ('.\\Report\\')
    now = time.strftime("%y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    filename = report_path +  now + '_report.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = u"测试结果", description = u"音乐车机测试结果",verbosity=2)
    runner.run(suite)
    logger = logging.getLogger("my_test")
    logger.setLevel(logging.DEBUG)
    # 写一个handler,用于写日志
    test_log_txt = logging.FileHandler("I:\\text_log\\log.txt")
    test_log_txt.setLevel(logging.DEBUG)
    # 写一个handler,用于写日志到控制台
    test_log = logging.StreamHandler()
    test_log_txt.setLevel(logging.DEBUG)
    # 定义一个handler输入日志格式
    Format_handler = logging.Formatter("%(asctime)s-%(name)s-%(Levelname)s-%(messages)s")
    test_log_txt.setFormatter(Format_handler)
    test_log.setFormatter(Format_handler)
    logger.addHandler(test_log_txt)
    logging._addHandlerRef(test_log)
    fp.close()
