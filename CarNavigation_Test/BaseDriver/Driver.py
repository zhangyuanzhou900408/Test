from time import sleep
from appium import webdriver

class Driver_Test:
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'm1'
        desired_caps['appPackage'] = 'com.autoai.car'
        desired_caps['appActivity'] = 'com.autoai.car.MainActivity'
        desired_caps['appWaitActivity'] = 'com.autoai.car.MainActivity'
        desired_caps['uuid'] = '0123456789ABCDEF'
        #desired_caps['dontStopAppOnReset'] = False  # True不关闭应用
        #desired_caps['autoGrantPermissions'] = True  # 自动获取权限
        #desired_caps["noReset"] = False  # True不用每次重置
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(5)
     # Quits the driver and closes every associated window
    def tearDown(self):
        self.driver.quit()
      # 获取驱动
    def get_driver(self):
        return self.driver













