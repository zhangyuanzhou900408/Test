from selenium.webdriver.common.by import By
from conf.Driver_app import  AndrionTest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import yaml
import os,re
import yaml
import pygame, sys
import time
import os,json
import conf.read_file
from utg.operation_json import OperationJson
import pyttsx3


# 当前脚本路径

basepath = 'D:\\python\\Projects\\Link\\Pages\\Elements'

#yaml文件夹
yamlPagesPath = os.path.join(basepath,'homepage.yaml')

class Action(AndrionTest):
    crash_id = "android:id/parentPanel"
    def __init__(self):
        AndrionTest.__init__(self)
        self.json_id = OperationJson()
    def restart_APP(self):
        '''重启app'''
        self.driver.close_app()
        sleep(5)
        self.driver.launch_app()
        sleep(5)

    def close(self):
        '''关闭appium webdriver'''
        self.driver.quit()

    def find_element_name(self, loc):
        '''重写name定位'''
        try:
            return self.driver.find_element_by_name(loc)
        except Exception as e:
            print("未找到%s" % (loc))

    def find_element_id(self, loc1):
        '''重写id定位'''
        try:
            return self.driver.find_element_by_id(loc1)
        except Exception as e:
            return False
             #print("未找到%s" % (loc1))

    def find_element_xpath(self, loc2):
        '''重写xpath定位'''
        try:
            return self.driver.find_element_by_xpath(loc2)
        except Exception as e:
            pass
            #print("未找到%s" % (loc2))

    def slide(self, x1_location, y1_location, x2_location, y2_location):
        '''滑动封装'''
        try:
            x = self.driver.get_window_size()['width']
            y = self.driver.get_window_size()['height']
            f = self.driver.swipe(x1_location * x, y1_location * y, x2_location * x, y2_location * y , 1000)
            return f
        except Exception as e:
            print("没有滑动")

    def search(self,Input_box,content):
        ''' 输入文本封装'''
        try:
            return self.driver.find_element_by_id(Input_box).send_keys(content)
        except Exception as e:
            print('搜索出错')

    def parseyaml(self,name):
        '''遍历yaml文件内容'''
        try:
            with open(yamlPagesPath, 'r', encoding='utf-8') as f:
                d = yaml.load(f)
                cm = d[name]
                ID = cm["xpath"]
                return ID
        except Exception as e:
            print('搜索出错:')

    def voice_case(self,filepath,id):
        #列出filepath这个路径下的所有文件
        pathDir = os.listdir(filepath)
        #print(pathDir)
        data_list = sorted(pathDir,key = lambda i:int(re.match(r'(\d+)',i).group()))
        #print(data_list)
        data = (data_list[id])
        #print(data)
        pygame.mixer.init()
        pygame.mixer.music.load(filepath +'\\%s' % data)
        pygame.mixer.music.play()
        time.sleep(3)
        pygame.mixer.music.stop()
        return pygame.mixer.music.play
    def system_player(self,filepath,id):
        # 列出filepath这个路径下的所有文件
        pathDir = os.listdir(filepath)
        # print(pathDir)
        data_list = sorted(pathDir, key=lambda i: int(re.match(r'(\d+)', i).group()))
        #print(data_list)
        data = (data_list[id])
        #print(data )
        play = os.system(filepath +'\\%s' % data)
        return play

    def Voice_id(self,filepath):
        # 列出filepath这个路径下的所有文件
        pathDir = os.listdir(filepath)
        # print(pathDir)
        data_list = sorted(pathDir, key=lambda i: int(re.match(r'(\d+)', i).group()))
        # print(data_list)
        data = (data_list)
        return data

    def Exist(self,element):
        '''判断元素是否存在'''
        time.sleep(3)
        flag = None
        try:
            if self.find_element_id(self.json_id.get_data(element)):
                #print("元素1存在")
                data = self.find_element_id(self.json_id.get_data(element))
                flag = True
        except:
            #print("元素不存在")
            flag = False
        return flag

    def test_Toast(self,toast_id):
        '''判断toast是否出现'''
        try:
            WebDriverWait(self.driver,timeout=30,poll_frequency=0.5).until(EC.presence_of_element_located(toast_id))
            return True
        except:
            return False
    def Main_Activity(self,id):
        '''主页面是否出现'''
        flag = None
        if self.driver.wait_activity(self.json_id,10):
            flag =  True
        else:
            flag =False
        return flag



    def news(self,id1,id2,id3):
        self.driver.tap(id1,id2,id3);
    # 测试是否进入到music界面
    def QQmusic(self,id):
        time.sleep(6)
        flag = None
        if self.find_element_id(self.json_id.get_data(id)):
            flag = True
        else:
            flag = False
        return flag
    # 是否进入FM界面
    def FM(self, id):
        flag = None
        if self.find_element_id(self.json_id.get_data(id)):
             flag = True
             #print("找到了FM元素")
        else:
            flag = False
            #print("没有找到FM元素")
        return flag
     #是否进入到语音界面吗
    def Voices(self,id):
        flag = None
        if self.find_element_id(self.json_id.get_data(id)):
            flag = True
        # elif self.system_player('F:\\music3', 34):
        #     print("再唤醒一次")
        # elif self.restart_APP():
        #     flag = True
        else:
            #print("没有进入语音界面，唤醒失败")
            flag = False
        return flag
        #time.sleep(5)
        #self.find_element_id(self.json_id.get_data(id)).click()
    #FM文本内容
    def FM_title(self,id,id2):
        data = None
        time.sleep(2)
        if self.FM("FM_Switch"):
            data = self.find_element_id(self.json_id.get_data(id)).get_attribute("text")
            #print(data)
        elif self.FM("Search_button"):
            data = self.find_element_id(self.json_id.get_data(id2)).get_attribute("text")
            #print(data)
        else:
            if self.get_text2("QQmusic_title", "toast_id", "Confirm_button_id","QQmusic_one_title"):
                data = ("没有进入Fm界面,进入QQ音乐界面" )
            else:
                data = ("没有进入Fm界面,进入其他界面")
        return data

    # 获取QQ音乐界面文本内容
    def get_text2(self, id,toast_id,id2,id3):
        flag = None
        time.sleep(3)
        if self.find_element_id(self.json_id.get_data(toast_id)): # 弹框是否需要会员
            self.find_element_id(self.json_id.get_data(id2)).click()
            time.sleep(2)
            if self.QQmusic("QQmusic_Collection"):
                flag = self.find_element_id(self.json_id.get_data(id)).get_attribute("text")
                #print(flag)
            elif self.QQmusic("local_QQmusic"):
                flag = self.find_element_id(self.json_id.get_data(id3)).get_attribute("text")
                #print(flag)
        else:
            if self.QQmusic("QQmusic_Collection"):
                flag = self.find_element_id(self.json_id.get_data(id)).get_attribute("text")
                #print(flag)
            elif self.QQmusic("local_QQmusic"):
                flag =self.find_element_id(self.json_id.get_data(id3)).get_attribute("text")
                #print(flag)
            else:
                flag = False

        return flag
    #获取语音转换文本
    def Voices_txt(self,id):
        flag = None
        time.sleep(3)
        if self.find_element_id(self.json_id.get_data(id)): #是否出现语音文本界面
            flag =  self.find_element_id(self.json_id.get_data(id)).get_attribute("text") #获取文本
        else:
            time.sleep(3)
            self.system_player('H:\\music3', 1)
            flag = False
            sleep(8)
        return flag
   # 获取tts播报文本
   #  def Voices_text(self, id):
   #      text = None
   #      time.sleep(3)
   #      if self.find_element_id(self.json_id.get_data(id)):  # 是否出现语音文本界面
   #          text = self.find_element_id(self.json_id.get_data(id)).get_attribute("txt")
   #
   #      else:
   #          self.system_player('F:\\music3', 36)
   #      return text
   #      print("进入文本")
   #      print(data)




#cm = Action()
#cm.FM_title("FM_title","FM_one_title")
# cm.pyttsx4('H:\\music00',10)
#cm.get_text2("QQmusic_title", "toast_id", "Confirm_button_id", "QQmusic_one_title")
