# import os,re
# import pygame
# import time
# def eachFile(filepath,id):
#     pathDir = os.listdir(filepath)
#     data_list = sorted(pathDir,key = lambda i:int(re.match(r'(\d+)',i).group()))
#     data = (data_list[id])
#     print( pathDir[id])
#     for i in range(1,116):
#         print(i)
#         pygame.mixer.init()
#         time.sleep(3)
#         pygame.mixer.music.load(filepath + '\\%d.mp3' %i )
#         pygame.mixer.music.play()
#         time.sleep(3)
#         pygame.mixer.music.stop()
#     return pathDir[id]
#
#         #for i in range(0,35):
#             #print(i)
#             #child = os.path.join('%s\%s' % (filepath, allDir[i]))
#             #print(child)
#     #return child
# File = eachFile('F:\\music1',115)

