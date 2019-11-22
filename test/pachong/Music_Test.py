import time
import json
import re
from lxml import etree
import requests

url_string = "https://y.qq.com/n/yqq/toplist/4.html"
headrs = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
requests.packages.urllib3.disable_warnings()
resopte = requests.get(url_string,headers=headrs,verify=False)
print(resopte.text)
trees = etree.HTML(resopte.text)
html_data = trees.xpath("/html/body/div[2]/div[2]/div[3]/ul[2]/li[1]/div/div[4]/span/a[1]")
print(html_data)



