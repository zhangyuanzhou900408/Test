import yaml
import os
import json
# 当前脚本路径

basepath = 'D:\\python\\Projects\\Link\\Pages\\Elements'

#yaml文件夹
yamlPagesPath = os.path.join(basepath,'homepage.yaml')
def parseyaml(name):
    '''遍历yaml文件内容'''
    with open(yamlPagesPath, 'r', encoding='utf-8') as f:
        d = yaml.load(f)
        print(d[name])
        cm = d[name]
        dm = cm['xpath']
        print(dm)
parseyaml('CheYuebaoMusicFM')