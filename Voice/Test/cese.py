from gtts import gTTS
import os
import re
import time
from colorama import Fore, Back, Style
#颜色设置
# for color in ['GREEN', 'RED', 'BLUE', 'YELLOW', 'WHITE']:
#     print (getattr(Fore, 'BLUE'), "It's color will be")
#     #print (getattr(Back, color), "It's color will be", color)
#     print (Style.RESET_ALL)


#把文字转音频1
path = "H:\\song.txt"
with open (path,"r", encoding ="UTF-8" ) as f :
    text = f.readlines()
    #print(text)
    count = 289
for line in text:
      p1 = line.strip("\n")
      temp = p1.split(",")
      #print(temp)
      #count = 0
      for mm in temp:
         #count += 1
         MM = mm.replace("\"", "")  # 去掉字符串中的双引号
         #print(MM)
         count += 1
         time.sleep(2)
         tts = gTTS(text=MM,lang="zh-tw",slow=False)
         Broad = (str(count) + "." + mm)
         print(Broad)
         tts.save("H:\\Song\\%s.mp3" % Broad)
# mm=["播放莫文蔚的我的天"]
# for i in mm:
#     tts = gTTS(text = i, lang="zh-tw", slow=False,lang_check= "check")
#     Broad = (str(19) + "." + i)
#     print(Broad)
#     tts.save("H:\\music99\\%s.mp3" % Broad)
#把文字转音频2
# path = "H:\\00.txt"
# with open (path,"r", encoding ="UTF-8" ) as f :
#     text = f.readlines()
#     #print(line)
#     count = 0
# for line in text:
#       p1 = line.strip("\n")
#       temp = p1.split(",")
#       #count = 0
#       for mm in temp:
#           count += 1
#           tts = gTTS(text=mm,lang="zh-tw",slow=False)
#           Broad = (str(count) + "." + mm)
#           print(Broad)
#           tts.save("H:\\music00\\%s.mp3" % Broad)
# import win32com.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("播放张靓颖的歌")
#speaker.Speak(mm)
# path = "G:\\siweifile\\si_three.txt"
# with open (path,"r", encoding ="UTF-8" ) as f :
#     text = f.readlines()
#     #print(text)
#     for line in text:
#         #print(line)
#         p1 = line.strip("\n")
#         temp = p1.split(",")
#         #print(temp)
#         for  mm in temp:
#            #print(mm)
#            speaker = win32com.client.Dispatch("SAPI.SpVoice")
#            speaker.Speak(mm)


# import pyttsx3
# engine = pyttsx3.init()
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate+(-60))
# engine.say("hello dragon")
# engine.save("H:\\hello dragon.mp3" )
# engine.runAndWait()
