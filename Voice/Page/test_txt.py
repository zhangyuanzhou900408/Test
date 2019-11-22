import sys
import win32com.client
from gtts import gTTS
import pyttsx3
import codecs
#获取txt文件中的文件转换成单个txt
class Text:
    def test_text(self,path):
        f=  codecs.open(path ,"r", encoding='UTF-8')
        text = f.readlines()
        for i in range(0,35):
            with open('F:\\txt6\\%d.txt' % i,'w') as fp:
                text_data = fp.write(text[i])
        return text_data

# if __name__ == '__main__':
#      try_text = Text()
#      try_text.test_text("F:\\00.txt")











