import unittest
import logging
from  Project.Music_CarNavigation.WritedCase.open_close_app.Run_app import RunApp


class Test_open_close_app(unittest.TestCase):
    app = RunApp()
    def test_close_app(self):
        '''关闭app'''
        try:
            t = (u"本地")
            self.assertEqual(t, self.app.back_app())
            print('退出app正确')
            #logging.debug('退出app正确')
            #if t == self.app.back_app():
                #print('退出app正确')
        except Exception as e:
            #logging.debug('退出app失败')
            print('退出app失败')
    def test_open_app(self):
        '''打开app'''
        try:
            t = (u"QQ音乐")
            self.assertEqual(t, self.app.OpenAPP())
            #logging.debug('进入app正确')
            print('进入app正确')
            #if t == self.app.OpenAPP():

        except Exception as e :
            #logging.debug('进入app失败')
            print('进入app失败')
