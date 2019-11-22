from appium import webdriver
from time import sleep
import unittest
import os
import json
import yaml
# 当前脚本路径
basepath = os.path.dirname(os.path.relpath(__file__))
#yaml文件夹
yamlPagesPath = os.path.join(basepath,'Elements')

class AndrionTest:
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = 'm1'
        desired_caps['appPackage'] = 'com.hongfans.mobileconnet'
        desired_caps['appActivity'] = 'com.hongfans.mobileconnet.SplashActivity'
        desired_caps['appWaitActivity'] = 'com.hongfans.mobileconnet.SplashActivity'
        desired_caps['uuid'] = '79AEALK35EUE'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(5)


    def tearDown(self):
       self.driver.quit()
    def get_driver(self):
        return self.driver
