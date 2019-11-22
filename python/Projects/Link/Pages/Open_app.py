from time import sleep
from BaseDriver.operation_json import OperationJson
from BaseDriver.Driver import APP_Basic
import json

class RunApp(APP_Basic):
    def __init__(self):
        APP_Basic.__init__(self)
    def OpenAPP(self):
        '''打开app'''
        sleep(1)
        self.find_id("Start.json", "local_music_id").click()
        sleep(1)
        m = self.find_xpath("Start.json","fm_xpath").get_attribute("text") #获取节目Tab文本
        t= "".join(m.split())
        print(t)
        return t

    def back_app(self):
        '''退出app'''
        self.driver.press_keycode(4) # 发送返回按钮
        sleep(1)
        n = self.find_id("Start.json","local_music_id").get_attribute("text")#获取本地Tab文本
        print(n)
        return n

    #def QuitAPP(self):
        '''关闭app'''
        #self.Close_APP()