import requests
import json


class RunMain:
    """含有构造器"""
    def __init__(self,url,method,data=None):
        self.t = self.run_main(url, method, data)
    # 发送 post请求
    def send_post(self, url, data):
        r = requests.post(url=url, data=data)
        result = r.json()
        return json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)
   # 发送get 请求
    def send_get(self, url, data):
        r = requests.get(url=url, params=data)
        result = r.json()
        return json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)
        # 利用json.dumps将响应数据进行json格式的编码解析
        # indent=2将输出结果缩进2个字符显示
        # sort_keys=False，输出结果是否按照关键字排序
        # json.dumps 序列化时对中文默认使用的ascii编码，ensure_ascii=False才会输出中文
        # return result
    # 合并 发送get 和post请求
    def run_main(self, url, method, data=None):
        if method == 'GET':
            r = self.send_get(url, data)
        else:
            r = self.send_post(url, data)
        return r
if __name__ == '__main__':
    url = 'http://res.hongfans.cn/v1/home'
    #cm = RunMain()
    data1 = {"n":"1", "category_id": "","album_id":"","page": "1", "ad_plugin_ver":"1.0.2","androidId": "a369d4ad9a3e0000", "app_key": "B1HYTY1603000000", "app_ver": "3.3.1.3.0", "dc": "3d6874a056abc220a4d2ae027d3ae8067c9994601e610075cbefd43ff095a1c4", "dev_uuid": "00000000 - 6264 - c302 - ffff - ffffe6992eeb", "display": "OPM1.171019.011", "iccid": "89860617020012434530", "imei": "868938030982252", "imsi": "46006", "mac": "020000000000", "model": "Redmi Note 5", "net_type": "Wi - Fi", "os_ver": "8.1.0", "plugin_ver": "1.0.13", "timestamp": "1534847923", "tinker_ver":"1.0.4"}
    print(data1)
    demo = RunMain(url,'GET', data1)
    #print(demo.t)


