
from time import sleep
from Config.operation_json import OperationJson
from Config.Basic_Site import APP_Basic

class RunApp(APP_Basic):
    def __init__(self):
        APP_Basic.__init__(self)
    def OpenAPP(self):
        '''打开app'''
        sleep(3)
        self.find_xpath("H:\\python_test\\CarNavigation_Test\\Helper\\Start.json", "local_music_xpath").click()
        m = self.find_id("H:\\python_test\\CarNavigation_Test\\Helper\\Start.json","QQ_music").get_attribute("text") #获取QQ音乐Tab文本
        print(m)
        return m

    def back_app(self):
        self.driver.press_keycode(4) # 发送返回按钮
        sleep(3)
        n = self.find_xpath("H:\\python_test\\CarNavigation_Test\\Helper\\Start.json","local_music_xpath").get_attribute("text")#获取本地Tab文本
        print(n)
        return n

    def QuitAPP(self):
        '''关闭app'''
        self.Close_APP()


