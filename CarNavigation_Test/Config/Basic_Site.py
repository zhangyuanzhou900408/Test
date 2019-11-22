import json
from datetime import time
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BaseDriver.Driver import Driver_Test
from Config.operation_json import OperationJson
class APP_Basic(Driver_Test):
    def __init__(self):
        Driver_Test.__init__(self)
        self.json_id = OperationJson()
    def Close_APP(self):
        '''重启app'''
        self.driver.close_app()
        sleep(5)
    def restart_APP(self):
        self.driver.launch_app()
        sleep(5)

    def kill_app(self):
        '''关闭appium webdriver'''
        self.driver.quit()

    def background_app(self, time):
        '''应用置于后台运行time时间'''
        self.driver.background_app(time)

    def clear(self):
        '''清除输入的内容'''
        self.driver.element.clear()

    def find_id(self,file,id):
        '''查找元素id'''
        data = self.driver.find_element_by_id(self.get_data(file,id))
        return data

    def find_xpath(self,file,xpath):
        '''查找元素xpath'''
        data = self.driver.find_element_by_xpath(self.get_data(file,xpath))
        return data


    def send_keys(self,xpath,*value):
        '''获取元素并输入值'''
        self.find_xpath(xpath).send_keys(*value)

    def find_name(self,name):
        '''通过name查找'''
        return self.driver.find_element_by_name(name)

    def get_data(self, file,id):
        '''获取json文件中的id值'''
        with open(file) as fp:
            data = json.load(fp)
        data_json = data[id]
        return data_json

    def  Slide(self,start_x,start_y,end_x,end_y):
        '''获取屏幕宽/高,进行屏幕滑动'''
        #获取屏幕宽
        screen_x = self.driver.get_window_size()['width']
        # 获取屏幕高
        screen_y = self.driver.get_window_size()['high']
        #移动的距离
        Slide_size =self.driver.swipe(start_x*screen_x,start_y*screen_y,end_x*screen_x,end_y*screen_y)
        return Slide_size

    def Exist(self,xpath):
        '''判断元素是否存在'''
        sleep(3)
        if self.find_xpath(xpath):
            print("出现元素")
        else:
            print("没有出现元素")
    def Text_Content(self):
        '''判断元素是否出现'''
        if self.Exist() == True:
            #获取元素文本内容
            data = self.find_id().get_attribute("text")
        return data

    def test_Toast(self,toast_id):
        '''判断toast是否出现'''
        falg = None
        try:
            WebDriverWait(self.driver,timeout=30,poll_frequency=0.5).until(EC.presence_of_element_located(toast_id))
            falg = True
        except:
            falg = False
        return falg

    # 获取toast信息，报错
    def find_toast(self, message):
        # mes = '//*[@text="请输入账号"]'
         elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, message))
         print (elem)



    # 获取当前activity的名称
    def get_current_activity_name(self):
        activity_name = self.driver.current_activity
        print('Current activity name is: %s' % activity_name)
        return activity_name

