# import os,json
# import datetime
# import time
# import csv
#import
# from conf.Driver_app import  AndrionTest
# from utg.operation_json import OperationJson
# print([n+m for n in "sda" for m in "refc"])
class People:
    def __init__(self,name,age):
        try:
            if not isinstance(name,str):
                pass
        except Exception as i :
            print("name 必须为str类型" + i)
        try:
           if not isinstance(age,int):
               pass
        except Exception as i:
            print("name 必须为int类型" + i)
        else:
            print("没有异常")

        self.name = name
        self.age = age
p = People(21,21)
# class Action(AndrionTest):
#     crash_id = "android:id/parentPanel"
#     def __init__(self):
#         AndrionTest.__init__(self)
#         self.json_id = OperationJson()
#     def restart_APP(self):
#         '''重启app'''
#         self.driver.close_app()
#         time.sleep(5)
#         self.driver.launch_app()
#         time.sleep(5)
#     def close(self):
#         '''关闭appium webdriver'''
#         self.driver.quit()
#
#     #安装耗时：
#     def installTime(self,serial,pkgName):
#         print('\n' + '============================')
#         push App(serial)
#         starttime = datetime.datetime.now().strftime("%y-%m-%d %H：%M：%S")
#         installApp(serial)  # 此处调用pminstall命令
#         endtime = datetime.datetime.now().strftime("%y-%m-%d %H：%M：%S")
#         print(pkgName, '安装耗时：', (endtime - starttime).total_seconds(), '秒')
#         time.sleep(1)
#         print('============================')
#
#     #首次启动耗时：
#     def firstStart(self,serial):#首次安装之后启动
#        print('\n'+'============================')
#        for i in range(5):#测试次数
#            i=i+1
#            print('---第%s次安装启动测试---'%i)
#            os.system('adb-s%sshellpmclear%s'%(serial,pkgName))
#            tt=os.popen('adb-s%sshellamstart-W%s'%(serial,appStartActivity))
#        for t in tt.readlines()[-8:-2]:
#           if t!='\n':\
#              print('首次安装启动耗时：',t.strip(),'ms')
#           time.sleep(1)
#           print('============================')
#     #冷启动耗时：
#     def coldStart(self,serial):
#         print('\n' + '============================')
#         for i in range(times):
#             i = i + 1
#             print('---第%s次冷启动测试---' % i)
#             os.system('adb-s%sshellamforce-stop%s' % (serial, pkgName))
#             tt = os.popen('adb-s%sshellamstart-W%s' % (serial, appStartActivity))
#             for t in tt.readlines()[-8:-2]:
#                 if t != '\n':
#                     print('冷启动耗时：', t.strip(), 'ms')
#                     time.sleep(1)
#                     print( "== == == == == == == == == == == == == ==")
#     #热启动耗时
#     def warmStart(self,serial):
#         print('\n' + '============================')
#         for i in range(times):
#             i = i + 1
#             print('---第%s次热启动测试---' % i)
#             os.system('adb-s%sshellinputkeyeventKEYCODE_HOME' % serial)
#             tt = os.popen('adb-s%sshellamstart-W%s' % (serial, appStartActivity))
#             for t in tt.readlines()[-8:-2]:
#                 if t != '\n':
#                     print('热启动耗时:', t.strip(), 'ms')
#                     time.sleep(1)
#         print("== == == == == == == == == == == == == ==")
#     def Test_time(self):
#         self.system_player('H:\\music3', 0)  # 小新您好


