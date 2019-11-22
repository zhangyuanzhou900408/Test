import requests
import time
import hashlib
import json
Name = ["刘德华", "张学友", "郭富城", "黎明"]
descr = ["播放", "搜索", "我要听", "我想听", "来一首", "来一个", "来一段", "来一曲", "来首", "来个", "来段", "来曲"]
# for searchName in Name:
#     print(searchName)
# for des in descr:
#     print(des)
def formatUrlAndHeader(token,searchName,des=None,id=None):
    searchContent = searchName
    sn = "0123456789ABCDEF"
    # 只取时间戳的整数位
    md5 = hashlib.md5()
    md5.update(searchContent.encode('utf-8'))
    data = md5.hexdigest()
    t = str(time.time())[0:-8]
    token_data = token
    #print(type(t))
    #print(t)
    d = {
                "is_voice": "1",
                "page":"1",
                "page_size":"20",
                "keywords":searchContent,
                "type":"1",
                "app_key":"B1HYTY1603000000",
                "app_ver":"3.2.0.0.12",
                "dc":"d6e065fc26410613fb6b7cec75a721f82ef74ccea1e393f43a2f840aa5004fec",
                "timestamp":t
            }

    url = ("http://dddcar.hongfans.cn/api/v1/search/index?type=1&keywords=%s&page=%d&page_size=20&app_key=H2DJCJ1901000000&app_ver=V1.0.21&imei=867215041781713&pack_name=com.autoai.car&product_type=D9A&sn=%s&software_version=D9A_TY_1.0.84_20190911_Daily&timestamp=%s&token=%s&n=1"% (searchContent,id,sn,t,token))
    #url2 = ("http://dddcar.hongfans.cn/api/v1/search/index?type=1&keywords=%s&page=%d&page_size=20&app_key=H2DJCJ1901000000&app_ver=V1.0.21&imei=867215041781713&pack_name=com.autoai.car&product_type=D9A&sn=%s&software_version=D9A_TY_1.0.84_20190911_Daily&timestamp=%s&token=%s&n=1"% (searchContent,id,sn,t,token))
    return url

def Analytical_Data():
    list1 = []
    list2=[]
    data_url = formatUrlAndHeader("obZfrkmq7bddcbV2iEfW4o2PZYI%3D", "刘德华",id=0)
    data1 = requests.get(data_url).json()
    #lenght = len(data["data"]["list"])
    page = data1["data"]["total_pages"]
    json_data=json.dumps(data1,indent=2,sort_keys=True)
    # if data["code"] ==200:
    #     for j in range(lenght):
    #         list1.append(data["data"]["list"][j]["singer"])
    #         list1.append(data["data"]["list"][j]["name"])
            #print(dict(zip(list1,list2)))
            #dt = dict(zip(list1, list2))
        #print(list1)

    if data1["data"]["total_pages"]>1:
        if data1["code"] ==200:
            for i  in range(1,21):
                data_url2 = formatUrlAndHeader("obZfrkmq7bddcbV2iEfW4o2PZYI%3D", "刘德华", id=i)
                lenght = len(data1["data"]["list"])
                data1 = requests.get(data_url2).json()
                for j in range(lenght):
                 list1.append(data1["data"]["list"][j]["singer"])
                 list2.append(data1["data"]["list"][j]["name"])
                 print(dict(zip(list1, list2)))








DATA = Analytical_Data()
