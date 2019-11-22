import unittest
import logging
from Projects.Link.Pages.Open_app import RunApp
class Test_open_close_app(unittest.TestCase):
    app = RunApp()
    def test_close_app(self):
        '''关闭app'''
        t = (u"本地")
        n= self.app.back_app()
        self.assert_equal(n, t)
        print('退出app正确')
        #try:
            # t = (u"本地")
             #if self.assertEqual(t, self.app.back_app()):
        #     assert self.app.back_app() == t
        #         print('退出app正确')
        #         logging.debug('退出app正确')
        #     #if t == self.app.back_app():
        #         #print('退出app正确')
        #     print('退出app正确')
        # except Exception as e:
        #     logging.debug('退出app失败')
        #     print('退出app失败')
    def test_open_app(self):
        '''打开app'''
        try:
            t = (u"节目")
            if  self.assertEqual(self.app.OpenAPP,t):
                logging.debug('进入app正确')
                print('进入app正确')
            #elif  t == self.app.OpenAPP():
                #logging.debug('进入app正确')
                #print('进入app正确')
        except Exception as e :
            logging.debug('进入app失败')
            print('进入app失败')
            print(e)
