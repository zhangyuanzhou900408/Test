import unittest
from page.Configuration import RunMain
import HTMLTestRunner
import json
class TestMethod(unittest.TestCase):    # 定义一个类，继承自unittest.TestCase

    def setUp(self):
        url = 'http://res.hongfans.cn/v1/album_details'
        self.run = RunMain(url=url,method='GET') # 生成一个实例对象

    def test01(self):
        ''''''
        url = 'http://res.hongfans.cn/v1/choice_playlist'
        data = {"n":"1", "category_id": "","album_id":"","page": "1", "page_size":"28","ad_plugin_ver":"1.0.2","androidId": "a369d4ad9a3e0000", "app_key": "B1HYTY1603000000", "app_ver": "3.3.1.3.0", "dc": "3d6874a056abc220a4d2ae027d3ae8067c9994601e610075cbefd43ff095a1c4", "dev_uuid": "00000000 - 6264 - c302 - ffff - ffffe6992eeb", "display": "OPM1.171019.011", "iccid": "89860617020012434530", "imei": "868938030982252", "imsi": "46006", "mac": "020000000000", "model": "Redmi Note 5", "net_type": "Wi - Fi", "os_ver": "8.1.0", "plugin_ver": "1.0.13", "timestamp": "1534847923", "tinker_ver":"1.0.4"}

        r = self.run.run_main(url, 'GET', data) # 调用RunMain类中run_main方法
        print(r)
        re = json.loads(r)
        if re['code'] == 200:
            print("测试通过")
        else:
            print("测试失败")



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test01'))
    #suite.addTest(TestMethod('test02'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
