import pygame, sys
import time
import os,json
from time import sleep
from appium import webdriver
from BaseDriver.Driver import Action
from utg.xls import OperationExecl
from utg.operation_json import OperationJson
#button = "android:id/message"
from colorama import Fore, Back, Style
#['GREEN', 'RED', 'BLUE', 'YELLOW', 'WHITE']
#print(getattr(Fore, 'RED'), "It's color will be")
#测试语音识别
class Open_app(Action):
    text =    "//android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView"
    text_id = "//android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView"
    text1_id ="//android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView"
    def __init__(self):
        # file_name = 'F:\\HF.xls'
        # sheet_id = 0
        # self.data = OperationExecl(file_name,sheet_id)
        #self.json_id = OperationJson()
        Action.__init__(self)
    #执行完一个case就重启app
    def restartApp(self):
        MN = self.restart_APP()
        return MN

    def Open_APP(self):
        '''关闭app'''
        self.driver.close_app()


    def Test_news(self):
        time.sleep(8)
        for i in  range(100):
            #点击固定新闻标题
            self.driver.tap([(0,462),(768,560)], 100)
            time.sleep(5)
            for i in range(2):
                self.slide(1/2,6/8,1/2,1/8)
                time.sleep(1)
                self.slide(1/2,6/8,1/2,1/8)
                time.sleep(1)
                self.slide(1/2,6/8,1/2,1/8)
                time.sleep(1)
                self.slide(1/2,6/8,1/2,1/8)
                time.sleep(1)
                self.slide(1/2,7/8,1/2,1/8)
                time.sleep(1)
                # 点击返回按钮
            self.driver.tap([(26,76),(62,112)],100)
            time.sleep(3)
            self.slide(1/2, 3/8, 1/2, 7/8)
            print("第%d个新闻+ %i")








    测试唤醒
    def Wake_test(self):
        for i in range(20):
            sleep(6)
            self.system_player('H:\\music3', 0)
            sleep(3)
            if self.find_element_id(self.json_id.get_data("Awak_words")):
                data = self.find_element_id(self.json_id.get_data("Awak_words")).get_attribute("text")
                sleep(4.5)
                self.system_player('H:\\music3', 1)
                print("第%d个文本内容为：%s" % (i, data))
            else:
                print(getattr(Fore, 'RED'),"第%d个没有进入语音界面" % i)






     #测试本地命令词
#     def Voice_test(self):
#         for i in range(0, 157):
#             sleep(20)
#             self.system_player('H:\\music3', 0)
#             sleep(3)
#             if self.Voices("Voice_id"):  # 判断是否进入语音界面
#                 self.system_player('H:\\music1', i)  # 进入语音界面输入语音指令
#                 sleep(8)
#                 # data = self.get_text2("QQmusic_title")
#                 if self.Voices("text_id"):  # 是否出现文本
#                     content = self.find_element_xpath(self.text_id).get_attribute("text")
#                     print(content)
#                 #if self.find_element_xpath(self.text_id):
#                     data =  self.find_element_xpath(self.text_id).get_attribute("text")
#                     data1 = self.find_element_xpath(self.text1_id).get_attribute("text")
#                      #data = self.Voices_txt(self.text_id)
#                     # data1 = self.Voices_txt(self.text1_id)
#                     print(getattr(Fore, 'GREEN'),"第%d个文本内容为：%s" % (i, data) +"------"+"第%d个tts播报内容为：%s" % (i, data1))
#                 else:
#                     print(getattr(Fore, 'YELLOW'),'%d' % i + ":" + "录音录入失败或者其他问题")
#             else:
#                 print(getattr(Fore, 'RED'),'%d' % i + ":" + "没有进入语音界面")
#                 continue
#
#    #测试QQ音乐播放的内容
#     def Voice2_test(self):
#             for i in range(77,105):
#                 sleep(10)
#                 self.system_player('H:\\music3', 0)  # 小新您好
#                 sleep(3)
#                 if self.Voices("voice_id"):  # 判断是否进入语音界面
#                     sleep(2)
#                     self.system_player('H:\\music99', i)  # 语音界面输入语音指令
#                     time.sleep(4)
#                     if self.Voices_txt("text_id"):  # 判断语音录入的文本界面是否出现
#                         data1 = self.Voices_txt("text_id")
#                         sleep(8)
#                         data = self.get_text2("QQmusic_title", "toast_id", "Confirm_button_id", "QQmusic_one_title") #取QQ音乐播放歌曲的名称
#                         print("第%d个文本内容为：%s" % (i, data1) + "------" + "第%d首歌曲名称和歌手内容为：%s" % (i, data))
#                     elif self.Voices_txt("text1_id"): #语音网络网络重新语音输入一次播放内容
#                         sleep(1)
#                         self.system_player('H:\\music99', i)
#                         if self.Voices_txt("text_id"):  # 判断语音录入的文本界面是否出现
#                             data1 = self.Voices_txt("text_id")
#                             sleep(8)
#                             data = self.get_text2("QQmusic_title", "toast_id", "Confirm_button_id",
#                                                   "QQmusic_one_title")  # 取QQ音乐播放歌曲的名称
#                             print(getattr(Fore, 'GREEN'),"第%d个文本内容为：%s" % (i, data1) + "------" + "第%d首歌曲名称和歌手内容为：%s" % (i, data))
#                     else:
#                          print(getattr(Fore, 'YELLOW'),'%d' % i+":" +"语音输入不对或者没有录入成功")
#                          sleep(20)
#                 else:
#                     '''判断是否出现崩溃'''
#                     if self.find_element_id(self.json_id.get_data("crash_id")):
#                         self.find_element_id(self.json_id.get_data("Button_id")).click()
#                         data = self.find_element_id(self.json_id.get_data("crash_id")).get_attribute("text")
#                         print(getattr(Fore, 'RED'),'第%d' % i+":" + "没有进入语音界面" + "崩溃内容为%s" % data)
#                         sleep(20)
#                     #print('\033[0;31;40m第%d' % i + ":" + "没有进入语音界面\033[0m")
#                     else:
#                        print(getattr(Fore, 'RED'),'第%d' % i + ":" + "没有进入语音界面")
#                     sleep(20)
#                     continue
#             print("-------------------------音乐测试完成----------------------------------")
#
#
# # 测试fm播放内容
#     def Voice3_test(self):
#         for i in range(104, 146):
#             sleep(6.5)
#             self.system_player('H:\\music3', 0)  # 小新您好
#             sleep(3)
#             if self.Voices("voice_id") or self.Voices("voice_help"):  # 判断是否进入语音界面
#                 sleep(1)
#                 self.system_player('H:\\music', i)  # 语音界面输入语音指令
#                 time.sleep(3)
#                 if self.Voices_txt("text_id"):  # 判断语音录入的文本界面是否出现
#                     data1 = self.Voices_txt("text_id")
#                     sleep(6)
#                     data = self.FM_title("FM_title", "FM_one_title")# 取fm播放的内容和名称
#                     print("第%d个文本内容为：%s" % (i, data1) + "------" + "第%d个节目名称和表演者为：%s" % (i, data))
#                 elif self.Voices_txt("text3_id"):
#                     #sleep(1)
#                     self.system_player('H:\\music', i)
#                     if self.Voices_txt("text_id"):  # 判断语音录入的文本界面是否出现
#                         data1 = self.Voices_txt("text_id")
#                         sleep(8)
#                         data = self.get_text2("QQmusic_title", "toast_id", "Confirm_button_id",
#                                               "QQmusic_one_title")  # 取QQ音乐播放歌曲的名称
#                         print(getattr(Fore, 'GREEN'),"第%d个文本内容为：%s" % (i, data1) + "------" + "第%d首歌曲名称和歌手内容为：%s" % (i, data))
#                 else:
#                     print(getattr(Fore, 'YELLOW'),'%d' % i + ":" + "语音输入不对或者没有录入成功")
#             else:
#                 '''判断是否出现崩溃'''
#                 if self.find_element_id(self.json_id.get_data("crash_id")):
#                     self.find_element_id(self.json_id.get_data("Button_id")).click()
#                     data = self.find_element_id(self.json_id.get_data("crash_id")).get_attribute("text")
#                     print(getattr(Fore, 'RED'),'第%d' % i + ":" + "没有进入语音界面" + "崩溃内容为%s" % data)
#                 # print('\033[0;31;40m第%d' % i + ":" + "没有进入语音界面\033[0m")
#                 else:
#                     print(getattr(Fore, 'RED'),'第%d' % i + ":" + "没有进入语音界面")
#                 sleep(20)
#                 continue




cm = Open_app()
cm.Test_news()
#cm.Wake_test()
#cm.Voice2_test()
#time.sleep(10)
#cm.Voice3_test()



        # sleep(3)
        # for i in  range(1,16):
        #     self.voice_case('F:\\JF', 0)
        #     sleep(1)
        #     if self.Exist("voice_id"):
        #         print(i)
        #         print( "日志 ："+ "唤醒成功" )
        #         self.voice_case('F:\\JF', 1)
        #         sleep(6)
        #     else:
        #         print(i)
        #         print("日志："  + "唤醒失败")
        #         sleep(6)





        #data = self.Voice_id('F:\\txt3')
        # for i in range(15):
        #     for i in range(0,34):
        #         self.voice_case('F:\\music2',33)
        #         sleep(4)
        #         self.voice_case('F:\\txt3',i)
        #         print(i)
        #         sleep(6)
        #         if self.Exist("crash_id"):
        #            text = self.find_element_id(self.Exist("crash_id")).get_attribute('text')
        #            print("错误日志：" + text)
        #            break





    # 执行语音mp3
    # def Voice1_test(self):
    #     sleep(6)
    #     self.voice_case('F:\\music1',115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 0)
    #     if self.Exist("iphone_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1',1)
    #     if self.Exist("main_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1',115)
    #     sleep(2)
    #     self.voice_case('F:\\music1',2)
    #     if self.Exist("FM_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 3)
    #     if self.Exist("main_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 4)
    #     if self.Exist("FM_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 5)
    #     if self.Exist("main_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 6)
    #     if self.Exist("FM_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 7)
    #     if self.Exist("main_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 8)
    #     if self.Exist("AM_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 9)
    #     if self.Exist("main_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 10)
    #     if self.Exist("AM_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 11)
    #     if self.Exist("main_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 12)
    #     if self.Exist("Bluetooth_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 13)
    #     if self.Exist("main_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 14)
    #     if self.Exist("Bluetooth_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 17)
    #     if self.Exist("main_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 18)
    #     if self.Exist("Bluetooth_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 19)
    #     if self.Exist("main_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 20)
    #     if self.Exist("void") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 21)
    #     if self.Exist("main_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     sleep(3)
    #     self.voice_case('F:\\music1', 115)
    #     sleep(2)
    #     self.voice_case('F:\\music1', 22)
    #     if self.Exist("void") == True:
    #         print("pass")
    #     else:
    #         print("failed")
    #     self.voice_case('F:\\music1', 115)
    #     sleep(3)
    #     self.voice_case('F:\\music1', 23)
    #     if self.Exist("main_id") == True:
    #         print("pass")
    #     else:
    #         print("failed")



