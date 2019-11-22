from data.run_method import Runmethod
from data.get_data import GetData
from common.common_util import Common
from common.emailTest import Email
import json
class Runtest:
    def __init__(self):
        self.run_method = Runmethod()
        self.get_data = GetData()
        self.common_util = Common()
        self.test_email = Email()
    # 获取需要执行的数据
    def request_data(self):
        res = None
        count_pass = []
        count_filed = []
        line_number = self.get_data.get_case_line()
        for i in range(1,line_number):
            print(i)
            url = self.get_data.get_url(i) # 获取请求url
            #print(url)
            header = self.get_data.get_request_heared(i)   #获取请求头
            #print(header)
            data = self.get_data.get_data_for_jaon(i)  #获取请数据
            #print(data)
            request_way = self.get_data.get_method(i)  #获取请求方式
            #print(recategory_idquest_way)
            run = self.get_data.get_is_run(i) #获取是否执行
            #print(run)
            request_except = str(self.get_data.get_except_data(i)) #获取预期结果
            #print(type(request_except))
            #print(request_except)
            if run:
                res = self.run_method.run_main(request_way,url,data,header)
                # print(type(res))
                #print(res)
                #判断两个值是否包含关系
                if  self.common_util.Contrast_test(request_except,res):
                    self.get_data.get_results_value(i,"pass")
                    count_pass.append(i)
                else:
                    self.get_data.get_results_value(i,res)
                    Fail = count_filed.append(i)

        #print(len(count_pass))
        print("成功的case:%s个" %len(count_pass))
        #print(len(count_filed))
        print("失败的case:%s个"%len(count_filed))
        list = ['1026928681@qq.com',"2278680647@qq.com"]
        sub = "后台接口测试结果"
        content = ("成功的case:%s个;" %len(count_pass) + "失败的case:%s个;"%len(count_filed) +"通过率75%,失败率25%。")
        self.test_email.send_email(list,sub,content)
        return res







if __name__ == '__main__':
    test = Runtest()
    test.request_data()