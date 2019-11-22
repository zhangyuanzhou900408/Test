from appium import webdriver
from time import sleep
import unittest
import os
import json
import yaml

class AndrionTest:
    '''初始化连接器'''
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = 'm1'
        desired_caps['appPackage'] = 'com.hongfans.mobileconnect'
        desired_caps['appActivity'] = 'com.hongfans.mobileconnect.SplashActivity'
        desired_caps['appWaitActivity'] = 'com.hongfans.mobileconnect.SplashActivity'
        desired_caps['uuid'] = '79AEALK35EUE'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(5)



    def setUp(self):
        print("开始测试")

    def tearDown(self):
       self.driver.quit()

    def get_driver(self):
        return self.driver



