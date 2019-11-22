import requests
import json
# 获取结果集
class Runmethod:
    #获取post请求数据
    def post_main(self,url,data,header=None):
        res =None
        if header != None:
            result =  requests.post(url=url,data=data,headers=header).json()
            res = json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)
        else:
            result1 = requests.post(url=url,data=data).json()
            res = json.dumps(result1, indent=2, sort_keys=False, ensure_ascii=False)
        return res

    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            result3 = requests.get(url=url, data=data, headers=header).json()
            res = json.dumps(result3, indent=2, sort_keys=False, ensure_ascii=False)

        else:
            result4 = requests.get(url=url, data=data, headers=header).json()
            res = json.dumps(result4, indent=2, sort_keys=False, ensure_ascii=False)
        return res

    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'GET':
            res = self.get_main(url,data,header)
        else:
            res = self.post_main(url,data,header)
        return res
